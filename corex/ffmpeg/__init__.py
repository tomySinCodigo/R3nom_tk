import subprocess
from pathlib import Path
import tomllib
import json
from corex.conversor import Tiempos, Con


class FFmpeg:
    def __init__(self, rvideo:str, ffprobe='ffprobe'):
        self.setVideo(rvideo)
        self.setProbe(ffprobe)
        self.__configMiFFmpeg()

    def __configMiFFmpeg(self):
        self.TD = self._leeToml()

    def setProbe(self, exe:str):
        self.PROBE = Path(exe).as_posix()

    def setVideo(self, rvideo:str):
        self.rvideo = Path(rvideo)
        self.DATA = None

    def _leeToml(self):
        with open('corex/ffmpeg/ffmpeg.toml', 'rb') as file:
            return tomllib.load(file)
        
    def cmd(self, args:list) -> str:
        return subprocess.check_output(args, encoding='utf-8')
    
    def cnf(self, nom:str, titulo='config'):
        return self.TD[titulo].get(nom)
    
    def getRaw(self) -> dict:
        cmds = self.cnf('cmd info').split()
        data = self.cmd([self.PROBE, *cmds, self.rvideo.as_posix()])
        return json.loads(data)
    
    def getStreamRaw(self, nstream:int=0):
        """return info raw, nstream[0:video, 1:audio, 2:format, 3:all]"""
        rw = self.getRaw()
        streams = rw.get('streams')
        match nstream:
            case 0:
                return streams[0]
            case 1:
                return streams[1]
            case 2:
                return streams[2]
            case _:
                return rw
            
    def getData(self):
        rw = self.getRaw()
        tv = rw['streams'][0]
        ta = rw['streams'][1]

        def video(nom:str) -> str:
            return tv[nom]
        
        def audio(nom:str) -> str:
            return ta[nom]
        
        def fm(nom:str) -> str:
            return rw['format'].get(nom)
        
        return {
            'format':{
                'bitrate':fm('bit_rate'),
                'duration':fm('duration'),
                'size':fm('size'),
                'tags':fm('tags')
            },
            'video':{
                'bitrate':video('bit_rate'),
                'codec':video('codec_name'),
                'codec name':video('codec_tag_string'),
                'duration':video('duration'),
                'height':video('coded_height'),
                'width':video('coded_width'),
                'ar':video('display_aspect_ratio'),
                'duration_ts':video('duration_ts'),
                'h':video('height'),
                'w':video('width'),
            },
            'audio':{
                'bitrate':audio('bit_rate'),
                'codec':audio('codec_name'),
            }
        }
    
    def getDataText(self):
        return json.dumps(self.getData(), indent=4)
    
    def genProperties(self):
        rw = self.getData()
        self.video = Video(rw)
        self.audio = Audio(rw)
        self.general = General(rw)
            

class Audio:
    def __init__(self, dataraw:dict):
        self.rw = dataraw
        self.__configAudio()

    def __configAudio(self):
        self._con = Con()
        self._ta = self.rw.get('audio')
        d = {
            'bitrate':self._con.unidad(self._ta.get('bitrate'))
        }
        self._ta.update(d)

    @property
    def bitrate(self) -> str:
        return self._ta.get('bitrate')[1] + "ps"
    
    @property
    def codec(self) -> str:
        return self._ta.get('codec')

    def getData(self):
        return json.dumps(self._ta, indent=4)


class Video:
    def __init__(self, dataraw:dict):
        self.rw = dataraw
        self.__configVideo()

    def __configVideo(self):
        self._con = Con()
        self._tim = Tiempos()
        self._tv = self.rw.get('video')
        dur = self._tim.mseg_ts(float(self._tv.get('duration')) * 1000)
        d = {
            'bitrate':self._con.unidad(self._tv.get('bitrate')),
            'duration':dur,
            't':self._tim.ts_cut(ts=dur)
        }
        self._tv.update(d)

    @property
    def bitrate(self) -> str:
        return self._tv.get('bitrate')[1] + "ps"
    @property
    def duration(self) -> str:
        return self._tv.get('duration')
    @property
    def codec(self) -> str:
        return self._tv.get('codec')
    @property
    def codecName(self) -> str:
        return self._tv.get('codec name')
    @property
    def height(self) -> str:
        return self._tv.get('height')
    @property
    def width(self) -> str:
        return self._tv.get('width')
    @property
    def t(self) -> str:
        return self._tv.get('t')
    
    def getData(self):
        return json.dumps(self._tv, indent=4)
    

class General:
    def __init__(self, dataraw:dict):
        self.rw = dataraw
        self.__configGeneral()

    def __configGeneral(self):
        self._con = Con()
        self._tim = Tiempos()
        self._fm = self.rw.get('format')
        dur = self._tim.mseg_ts(self._fm.get('duration'))
        d = {
            'bitrate':self._con.unidad(self._fm.get('bitrate')),
            'size':self._con.unidad(self._fm.get('size'), 1024),
            'duration':dur,
            't':self._tim.ts_cut(ts=dur)
        }
        self._fm.update(d)

    @property
    def bitrate(self) -> str:
        return self._fm.get('bitrate')[1] + "ps"
    @property
    def duration(self) -> str:
        return self._fm.get('duration')
    @property
    def size(self) -> str:
        return self._fm.get('size')

    @property
    def t(self) -> str:
        return self._fm.get('t')
    
    def getData(self):
        return json.dumps(self._fm, indent=4)