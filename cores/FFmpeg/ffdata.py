import subprocess
from pathlib import Path
import tomllib
import json


class FFData:
    def __init__(self, archivo, ffprobe="ffprobe.exe"):
        self.setFFProve(ffprobe)
        self.setVideo(archivo)
        self.TOM = self.leeToml()

    def setFFProve(self, exe:str):
        "ruta del exe de ffprobe"
        self.PROBE = Path(exe).as_posix()

    def setVideo(self, archivo:str):
        self.archivo = Path(archivo)
        self.VIDEO = self.archivo.as_posix()
        self.DATA_VIDEO = None

    def leeToml(self):
        with open("cores/FFmpeg/ffmpeg.toml", "rb") as file:
            return tomllib.load(file)
        
    def cmd(self, argums:list):
        return subprocess.check_output(argums, encoding="utf-8")
    
    def cnf(self, nom:str, titulo="config"):
        return self.TOM[titulo].get(nom)
    
    def getInfo(self):
        cmd = self.cnf("cmd info").split()
        data = self.cmd([self.PROBE, *cmd, self.VIDEO])
        self.DATA_VIDEO = json.loads(data)

    def _unidad(self, n:int, capital:bool=False) -> int:
        b = 1000
        for x in ["bt", "kb", "mb", "gb", "tb"]:
            if n < b:
                unidad = f"{x.capitalize()}" if capital else f"{x.lower()}"
                return f"{n:.2f}{unidad}"
            n /= b

    def raw(self, tipo="format"):
        """tipo: format, video, audio, all"""
        if tipo == "format":
            return self.DATA_VIDEO.get(tipo)
        elif tipo == "all":
            return self.DATA_VIDEO
        else:
            streams = self.DATA_VIDEO.get("streams")
            if tipo == "video":
                return streams[0]
            if tipo == "audio":
                return streams[1]
            
    def getRaw(self, tipo:str="format") -> dict:
        """obten solo info de campos seleccionados en toml[raw]"""
        raw = self.raw(tipo)
        li = self.TOM["raw"].get(tipo)
        return {elem:raw.get(elem) for elem in li}
    
    def getValue(self, nom:str, tipo:str="format") -> str:
        """tipo: format, video, audio, all"""
        return self.getRaw(tipo=tipo).get(nom)
    
    def getVideo(self, nom:str) -> str:
        """obten valores del stream de Video"""
        return self.getValue(nom, tipo="video")
    
    def get(self, pal:str) -> str:
        return self.getData().get(pal)
    
    def getData(self) -> dict:
        return {
            "duracion":self.getValue("duration"),
            "bitrate":self._unidad(int(self.getValue("bit_rate"))),
            "peso":self.getValue("size"),
            "bitratev":self._unidad(int(self.getVideo("bit_rate"))),
            "duracionv":self.getVideo("duration"),
            "alto":self.getVideo("height"),
            "ancho":self.getVideo("width"),
            "codecname":self.getVideo("codec_long_name"),
            "codec":self.getVideo("codec_name"),
            "asra":self.getVideo("display_aspect_ratio")
        }



if __name__ == '__main__':
    vd = "C:/Users/mortadela/Downloads/7276517264029.mp4"
    from pprint import pprint
    ff = FFData(vd)
    ff.getInfo()

    # RAW
    # pprint(ff.raw("all"))
    # print(type(ff.raw()))
    # pprint(ff.raw())

    # STREAMS (RAW)
    # rw = ff.getRaw("format")
    # rw = ff.getRaw("video")
    # pprint(rw)
    # rwa = ff.getRaw("audio")
    # pprint(rwa)

    # DATO
    # dur = ff.getVideo("duration")
    # print(dur)

    # para keys
    # pprint(ff.getData())
    print(ff.get("duracion"))
    print(ff.get("bitratev"))
    print(ff.get("alto"))