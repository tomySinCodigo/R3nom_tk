from pathlib import Path
import subprocess, json
from corex.conversor import Tiempos, Con


class VideoData:
    def __init__(self, raw:dict):
        self._rw = raw

    def getRaw(self):
        return {
            'video':{
                'codec':self.get('CompressorID'),
                'format':self.get('FileType'),
                'height':self.get('ImageHeight'),
                'width':self.get('ImageWidth'),
                'duration ts':f"{self.get('Duration')}.000",
            },
            'audio':{
                'format':self.get('AudioFormat'),
                # '':self.get(''),
                # '':self.get(''),
                # '':self.get('')
            },
            'general':{
                'bitrate':self.get('AvgBitrate'),
                'codec name':self.get('CompressorName'),
                'duration':self.get('MediaDuration'),
                'filesize':self.get('FileSize'),
                'size':self.get('MovieDataSize'),
                'height':self.get('SourceImageHeight'),
                'width':self.get('SourceImageWidth'),
                # 'height':self.get(''),
            }
        }
    
    def getRawText(self):
        return json.dumps(self.getRaw(), indent=4)
    
    def get(self, value:str) -> str:
        return self._rw.get(value)


class Video:
    def __init__(self, track_video:dict):
        self._tv = track_video
        self.__configVideo()

    def __configVideo(self):
        self._tim = Tiempos()
        self._con = Con()

        self.data = self._tv
        d = {
            't':self._tim.ts_cut(self._tv.get('duration ts'))
        }
        self.data.update(d)

    @property
    def duration(self) -> str:
        return self.data.get('duration ts')
    @property
    def codec(self) -> str:
        return self.data.get('codec')
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


class General:
    def __init__(self, track_general:dict):
        self._tg = track_general
        self.__configGeneral()

    def __configGeneral(self):
        self._tim = Tiempos()
        self._con = Con()

        self.data = self._tg
        d = {
            'bitrate': self._tg.get('bitrate').replace(" ", ""),
            'size': self._con.unidad(self._tg.get('size'), 1024),
            # 'filesize': self._tg.get('filesize'),
        }
        self.data.update(d)

    @property
    def bitrate(self) -> str:
        return self.data.get('bitrate')
    @property
    def size(self) -> str:
        return self.data.get('size')[1]
    @property
    def filesize(self) -> str:
        return self.data.get('filesize')
    @property
    def codec(self) -> str:
        return self.data.get('codec name')
    @property
    def duration(self) -> str:
        return self.data.get('duration')
    @property
    def width(self) -> str:
        return self.data.get('wdth')
    @property
    def height(self) -> str:
        return self.data.get('height')
    
    def getData(self):
        return json.dumps(self.data, indent=4)


class ExifTool:
    def __init__(self, video:str, ruta_exiftool:str="corex/exiftool/exiftool"):
        self.exe = Path(ruta_exiftool).as_posix()
        self.VIDEO = Path(video).as_posix()

    def cmd(self, argums:list) -> str:
        return subprocess.check_output(argums, encoding="utf-8")
    
    def _getRawText(self) -> str:
        return self.cmd([self.exe, "-s", self.VIDEO])

    def getRaw(self) -> dict:
        res = {}
        for linea in self._getRawText().split("\n"):
            if ":" in linea:
                c, v = linea.split(":", 1)
                res[c.strip()] = v.strip(" \n")
        return res
    
    def genProperties(self):
        self.data = VideoData(self.getRaw())
        self.video = Video(self.data.getRaw().get('video'))
        self.general = General(self.data.getRaw().get('general'))