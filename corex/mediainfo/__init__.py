from pathlib import Path
from corex.mediainfo.MediaInfoDLL3 import MediaInfo, Stream
import tomllib, json
from corex.conversor import Tiempos, Con


class VideoData:
    def __init__(self, raw):
        self.raw = raw

    def getRaw(self):
        return {
            'video':{
                'bitrate':self.get('BitRate'),
                'codec':self.get('Format'),
                'duration':self.get('Duration'),
                'duration ts':self.get('Duration/String3'),
                'ar':self.get('DisplayAspectRatio/String'),
                'height':self.get('Height'),
                'width':self.get('Width'),
            },
            'audio':{
                'bitrate':self.get('BitRate', 'audio'),
                'codec':self.get('Format', 'audio'),
                # '':self.get('', 'audio'),
            },
            'general':{
                'bitrate':self.get('BitRate', 'audio'),
                'duration':self.get('Duration/String1'),
                'size':self.get('FileSize', 'general'),
                'filesize':self.get('FileSize/String', 'general'),
                'format':self.get('Format', 'general'),
            },
            # 'menu':{
            #     '':self.get('', 'menu'),
            # },
        }

    def get(self, valor:str, track='video') -> str:
        return self.raw[track].get(valor)
    
    def getRawText(self):
        return json.dumps(self.getRaw(), indent=4)
    

class Video:
    def __init__(self, track_video:dict):
        self._tv = track_video
        self.__configVideo()

    def __configVideo(self):
        self._tim = Tiempos()
        self._con = Con()

        self.data = self._tv
        ts = self._tim.mseg_ts(self._tv.get('duration'))
        d = {
            'bitrate': self._con.unidad(self._tv.get('bitrate')),
            'duration': ts,
            't':self._tim.ts_cut(ts)
        }
        self.data.update(d)

    @property
    def bitrate(self) -> str:
        return self.data.get('bitrate')[1] + "ps"
    @property
    def duration(self) -> str:
        return self.data.get('duration')
    @property
    def codec(self) -> str:
        return self.data.get('codec')
    # @property
    # def codecName(self) -> str:
    #     return self.data.get('coding_name')
    @property
    def height(self) -> str:
        return self.data.get('height')
    @property
    def width(self) -> str:
        return self.data.get('width')
    @property
    def t(self) -> str:
        return self.data.get('t')
    
    def getData(self):
        return json.dumps(self.data, indent=4)
    

class Audio:
    def __init__(self, track_audio:dict):
        self._ta = track_audio
        self.__configAudio()

    def __configAudio(self):
        self._tim = Tiempos()
        self._con = Con()

        self.data = self._ta
        d = {
            'bitrate': self._con.unidad(self._ta.get('bitrate')),
        }
        self.data.update(d)

    @property
    def bitrate(self) -> str:
        return self.data.get('bitrate')[1] + "ps"

    @property
    def codec(self) -> str:
        return self.data.get('codec')
    

class General:
    def __init__(self, track_general:dict):
        self._tg = track_general
        self.__configGeneral()

    def __configGeneral(self):
        self._tim = Tiempos()
        self._con = Con()

        self.data = self._tg
        d = {
            'bitrate': self._con.unidad(self._tg.get('bitrate')),
            'size': self._con.unidad(self._tg.get('size'), 1024),
            'filesize': self._tg.get('filesize'),
        }
        self.data.update(d)

    @property
    def bitrate(self) -> str:
        return self.data.get('bitrate')[1] + "ps"
    @property
    def size(self) -> str:
        return self.data.get('size')[1]
    @property
    def filesize(self) -> str:
        return self.data.get('filesize')
    @property
    def format(self) -> str:
        return self.data.get('format')
    @property
    def duration(self) -> str:
        return self.data.get('duration')
    
    def getData(self):
        return json.dumps(self.data, indent=4)


class MiMediaInfo:
    def __init__(self, rvideo:str):
        self.rvideo = Path(rvideo)
        self.__configMiMediaInfo()

    def __configMiMediaInfo(self):
        self.dc = self._readToml()

    def getRaw(self) -> dict:
        """retorna informacion (RAW) de los streams del video"""
        self.MI = MediaInfo()
        self.MI.Open(self.rvideo.as_posix())
        dv = {'general':{},'video':{},'audio':{},'menu':{}}
        dv['menu'] = self._getStream('menu', Stream.Menu)
        dv['general'] = self._getStream('general', Stream.General)
        dv['video'] = self._getStream('video', Stream.Video)
        dv['audio'] = self._getStream('audio', Stream.Audio)
        self.MI.Close()
        return dv
    
    def getInform(self) -> str:
        """retorna un informe con los datos del video"""
        self.MI = MediaInfo()
        self.MI.Open(self.rvideo.as_posix())
        info = self.MI.Inform()
        self.MI.Close()
        return info

    def _getStream(self, stream:str, streamObj:Stream) -> dict:
        return {
            param:self.MI.Get(streamObj, 0, param) \
            for param in self.dc['parametros'].get(stream, {})
        }
    
    def _getParameters(self, i=0):
        self.MI = MediaInfo()
        self.MI.Open(self.rvideo.as_posix())
        info = self.MI.Option("info_Parameters")
        self.MI.Close()
        return info
    
    def getStreamRaw(self, ntrack:int=0) -> dict:
        """retorna informacion de los streams  ntrack[0:video, 1:audio, 2:general, 3:menu]"""
        dv = self.getRaw()
        match ntrack:
            case 0:track = 'video'
            case 1:track = 'audio'
            case 2:track = 'general'
            case 3:track = 'menu'
            case _: track = 'video'
        return dv.get(track)

    def _readToml(self):
        with open("./corex/mediainfo/mediainfo.toml", "rb") as f:
            return tomllib.load(f)
        
    def genProperties(self):
        """genera las variables (video, audio, general) para obtener propiedades del video"""
        self.data = VideoData(self.getRaw())
        streams = self.data.getRaw()
        self.video = Video(track_video=streams.get('video'))
        self.audio = Audio(track_audio=streams.get('audio'))
        self.general = General(track_general=streams.get('general'))

    def __str__(self):
        return f"""PROPERTIES
        VIDEO:bitrate, duration, codec, height, width, t
        AUDIO:bitrate, codec
        GENERAL:bitrate, size, filesize, format, duration
        
        MiMediaInfo
        .getRaw:{self.getRaw.__doc__}
        .getInform:{self.getInform.__doc__}
        .getStreamRaw:{self.getStreamRaw.__doc__}
        .genProperties:{self.genProperties.__doc__}\n"""