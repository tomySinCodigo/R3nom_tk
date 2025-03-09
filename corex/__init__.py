from pathlib import Path
from corex.mediainfo import MiMediaInfo
from corex.exiftool import ExifTool
from corex.mp4info import Mp4Info
from corex.ffmpeg import FFmpeg


class CoreMediaInfo:
    def __init__(self, rvideo:str, cmd=str):
        self.rvideo = rvideo
        self.cmd = cmd
        self.__configCoreMediaInfo()

    def __configCoreMediaInfo(self):
        self.mi = MiMediaInfo(self.rvideo)
        self.mi.genProperties()

    def getTranslate(self):
        v = self.mi.video
        d = {
            'duracion': v.t,
            'bitratev':v.bitrate,
            'alto':v.height,
            'ancho':v.width,
            'codecv':v.codec
        }
        return self._find(d)

    def _find(self, dc:dict) -> str:
        keyswords = [p for p in self.cmd.split('$') if len(p)>3]
        txt = self.cmd
        for key in keyswords:
            word = f'${key}$'
            if key in dc.keys():
                txt = txt.replace(word, str(dc[key]))
        return txt


class CoreMp4Info:
    def __init__(self, rvideo:str, cmd=str):
        self.rvideo = rvideo
        self.cmd = cmd
        self.__configCoreMp4Info()

    def __configCoreMp4Info(self):
        self.mp4i = Mp4Info(self.rvideo)
        self.mp4i.genProperties()

    def getTranslate(self):
        v = self.mp4i.video
        d = {
            'duracion':v.t,
            'bitratev':v.bitrate,
            'alto':v.height,
            'ancho':v.width,
            'codecv':v.codec,
            'bitratea':self.mp4i.audio.bitrate,
            'codeca':self.mp4i.audio.codec
        }
        return self._find(d)

    def _find(self, dc:dict) -> str:
        keyswords = [p for p in self.cmd.split('$') if len(p)>3]
        txt = self.cmd
        for key in keyswords:
            word = f'${key}$'
            if key in dc.keys():
                txt = txt.replace(word, str(dc[key]))
        return txt


class CoreNone:
    def __init__(self, rvideo:str, cmd:str):
        self.rvideo = rvideo
        self.cmd = cmd

    def _find(self, dc:dict) -> str:
        keyswords = [p for p in self.cmd.split('$') if len(p)>3]
        txt = self.cmd
        for key in keyswords:
            word = f'${key}$'
            if key in dc.keys():
                txt = txt.replace(word, str(dc[key]))
        return txt
    

class CoreFFmpeg(CoreNone):
    def __init__(self, rvideo:str, cmd:str):
        super().__init__(rvideo, cmd)
        self.__configCoreFFmpeg()

    def __configCoreFFmpeg(self):
        self.ff = FFmpeg(self.rvideo)
        self.ff.genProperties()

    def getTranslate(self):
        v = self.ff.video
        a = self.ff.audio
        g = self.ff.general
        d = {
            'duracion':v.t,
            'bitratev':v.bitrate,
            'alto':v.height,
            'ancho':v.width,
            'codecv':v.codec,
            'codeca':a.codec,
            'bitratea':a.bitrate,
            'bitrateg':g.bitrate,
            'duracionts':g.duration,
            'size':g.size,
            'duraciong':g.t,
        }
        return self._find(d)
    

class CoreExif(CoreNone):
    def __init__(self, rvideo:str, cmd:str):
        super().__init__(rvideo, cmd)
        self.__configCoreExif()

    def __configCoreExif(self):
        self.ex = ExifTool(self.rvideo)
        self.ex.genProperties()

    def getTranslate(self):
        v = self.ex.video
        g = self.ex.general
        # a = self.ex.audio
        d = {
            'duracion':v.t,
            'codec':v.codec,
            'alto':v.height,
            'ancho':v.width,
            'bitrateg':g.bitrate, # solo existe el general (no del video)
            'bitratev':g.bitrate, # solo copia del general
            'size':g.size,
            'filesize':g.filesize,
            'codecg':g.codec,
            'duraciong':g.duration,
            'height':g.height,
            'width':g.width,
            # '':g,
        }
        return self._find(d)


class Corex:
    def __init__(
        self, rvideo:str,
        core:str, cmd:str,
        tags:str
    ):
        self.tags = tags
        self.rvideo = rvideo
        self.core = core.lower()
        self.cmd = cmd
        self.__configCorex()

    def __configCorex(self):
        if '$tags$' in self.cmd:
            self.cmd = self.cmd.replace('$tags$', self.tags)
        match self.core:
            case "mediainfo":
                self.cx = CoreMediaInfo(self.rvideo, self.cmd)
            case "mp4info":
                self.cx = CoreMp4Info(self.rvideo, self.cmd)
            case "ffmpeg":
                self.cx = CoreFFmpeg(self.rvideo, self.cmd)
            case "exiftool":
                self.cx = CoreExif(self.rvideo, self.cmd)
            case _:
                self.cx = CoreMediaInfo(self.rvideo, self.cmd)
                
    def getTranslate(self):
        return self.cx.getTranslate()
    
    def getDoc_mediainfo(self):
        mi = MiMediaInfo(rvideo=self.rvideo)
        return mi
    

if __name__ == '__main__':
    from pprint import pprint
    print("test 1")