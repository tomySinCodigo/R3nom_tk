from pathlib import Path
import subprocess, json
from corex.conversor import Tiempos, Con

        
class VideoData:
    def __init__(self, dmp4=dict):
        """dmp4: es un diccionario obtenido con mp4info.getData()"""
        self.d_mp4 = dmp4

    def tracks(self, i=0):
        """retorna los datos de los tracks: video[i=0] y audio[i=1]"""
        return self.d_mp4.get('tracks')[i]
    
    def getRaw(self):
        """retorna los datos en formato json[dict], solo los relevantes RAW"""
        video = self.tracks()
        audio = self.tracks(1)
        v_sd = video.get('sample_descriptions')[0]
        a_sd = audio.get('sample_descriptions')[0]

        return {
            'video':{
                'bitrate':video['media'].get('bitrate'),
                'duration':video['media'].get('duration'),
                'duration_ms':video['media'].get('duration_ms'),
                'sample_count':video['media'].get('sample_count'),
                'timescale':video['media'].get('timescale'),
                'coding':v_sd.get('coding'),
                'coding_name':v_sd.get('coding_name'),
                'height':v_sd.get('height'),
                'width':v_sd.get('width'),
            },
            'audio':{
                'bitrate':audio['media'].get('bitrate'),
                'coding':a_sd.get('coding'),
                'coding_name':a_sd.get('mpeg_4_audio_object_type_name'),
            }
        }
    
    def getRawText(self):
        """retorna los datos obtenidos en .getRaw() en formato texto[str]"""
        return json.dumps(self.getRaw(), indent=4)


class Audio:
    def __init__(self, track_audio:dict):
        self._ta = track_audio
        self.__configAudio()

    def __configAudio(self):
        # self._tim = Tiempos()
        self._con = Con()
        self.data = self._ta
        d = {
            'bitrate': self._con.unidad(self._ta.get('bitrate'))
        }
        self.data.update(d)

    @property
    def bitrate(self) -> str:
        return self.data.get('bitrate')[1] + "ps"
    
    @property
    def codec(self) -> str:
        return self.data.get('coding')
    
    @property
    def codecName(self) -> str:
        return self.data.get('coding_name')

        
class Video:
    def __init__(self, track_video:dict):
        self._tv = track_video
        self.__configVideo()

    def __configVideo(self):
        self._tim = Tiempos()
        self._con = Con()

        self.data = self._tv
        ts = self._tim.mseg_ts(self._tv.get('duration_ms'))
        d = {
            'bitrate': self._con.unidad(self._tv.get('bitrate')),
            'duration_ms': ts,
            't':self._tim.ts_cut(ts)
        }
        self.data.update(d)
    
    @property
    def bitrate(self) -> str:
        return self.data.get('bitrate')[1] + "ps"
    @property
    def duration(self) -> str:
        return self.data.get('duration_ms')
    @property
    def codec(self) -> str:
        return self.data.get('coding')
    @property
    def codecName(self) -> str:
        return self.data.get('coding_name')
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
    


class Mp4Info:
    def __init__(self, rvideo:str, exe:str='corex/mp4info/mp4info'):
        """rvideo:es la ruta del video, exe:es la ruta del ejecutable mp4info.exe"""
        self.EXE = Path(exe).as_posix()
        self.RV = Path(rvideo)

    def cmdCheck(self, args:list) -> str:
        """salida del comando check_output"""
        return subprocess.check_output(args, encoding='utf-8')

    def getRaw(self) -> str:
        """retorna los datos en formato json[str], texto obtenido de aplicar em comando"""
        return self.cmdCheck([
            self.EXE, "--verbose", "--format", "json",
            self.RV.as_posix()
        ])
    
    def getData(self) -> dict:
        """retorna los datos en formato json[dict]"""
        return json.loads(self.getRaw())
    
    def getVideoData(self) -> VideoData:
        """retorn un Objeto VideoData con los datos del video"""
        return VideoData(self.getData())
    
    def genProperties(self):
        self.data = self.getVideoData()
        streams = self.data.getRaw()
        self.video = Video(track_video=streams.get('video'))
        self.audio = Audio(track_audio=streams.get('audio'))


if __name__ == '__main__':
    from pprint import pprint
    rv = "U:/test.mp4"
    mp = Mp4Info(rv, exe='mp4info')
    # pprint(mp.getData())
    # vd = mp.getVideoData()
    # pprint(vd.getRaw())
    # print(vd.getRawText())
    
    mp.genProperties()
    # print(mp.video.bitrate())
    pprint(mp.video.data)
    # print(mp.getRaw())