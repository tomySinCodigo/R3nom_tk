from pathlib import Path
from cores.mediainfo.MediaInfoDLL3 import MediaInfo, Stream
import tomllib


class MiVideo:
    def __init__(self, video_ruta:str):
        self.archivo = Path(video_ruta)
        self.dc = self.lee_toml()
        self.MI = MediaInfo()

    def lee_toml(self):
        with open("./cores/mediainfo/mediainfo.toml", "rb") as f:
            return tomllib.load(f)

    def extrae_data(self):
        """extrae informacion del video en DATA_VIDEO"""
        self.MI.Open(self.archivo.as_posix())
        self.DATA_VIDEO = {'general':{}, 'video':{}, 'audio':{}, 'menu':{}}
        self.dc = self.lee_toml()
        self._get_stream('menu', Stream.Menu)
        self._get_stream('general', Stream.General)
        self._get_stream('audio', Stream.Audio)
        self._get_stream('video', Stream.Video)
        self.MI.Close()
        
    def _get_stream(self, tipo:str, stream_tipo:Stream):
        for param in self.dc.get('parametros')[tipo]:
            self.DATA_VIDEO[tipo][param] = self.MI.Get(stream_tipo, 0, param)

    def obten_valor(self, clave:str, stream='video') -> str:
        """clave es el identificador del valor que necesites (en toml),
        stream:video,audio,general,menu"""
        res = self.DATA_VIDEO[stream].get(clave)
        if res.isnumeric():
            res = int(res)
        return res

    def _unidad(self, n:int, capital:bool=False) -> int:
        b = 1000
        for x in ["bt", "kb", "mb", "gb", "tb"]:
            if n < b:
                unidad = f"{x.capitalize()}" if capital else f"{x.lower()}"
                return f"{n:.2f}{unidad}"
            n /= b

    def fix(self, texto) -> str:
        dc = self.dc.get('config')
        if isinstance(texto, str):
            for c, v in dc.items():
                texto = texto.replace(c, v).strip()
        return texto

    def basico(self) -> dict:
        data = {}
        dc = self.dc.get("basico")
        for c, v in dc.items():
            data[c] = self.fix(self.obten_valor(v[0], v[1]))
        if '.' in data['tiempo texto']:
            data["duracion"] = data['tiempo texto'].strip("s")
        data['peso'] = self._unidad(int(data['pesoi']), False)
        data['folder'] = self.archivo.parent.as_posix()
        data['folder nombre'] = self.archivo.parent.name
        _tmp = dc.get("tiempo")
        data['timestamp'] = self.obten_valor(_tmp[0], _tmp[1])
        return data
    
    def version(self) -> str:
        return self.MI.Option("Info_Version")
    
    def informe(self) -> str:
        gral = self.raw()
        video = self.raw('video')
        audio = self.raw('audio')
        dgral = {
            # "Duration/String3":gral.get("Duration/String3"),
            "Duration/String5":gral.get("Duration/String5"),
            "BitRate/String":gral.get("BitRate/String"),
            "Format":gral.get("Format"),
            "FrameRate/String":gral.get("FrameRate/String"),
            # "":video.get(""),
        }
        dvideo = {
            "BitRate/String":video.get("BitRate/String"),
            "Duration/String1":video.get("Duration/String1"),
            "Duration/String3":video.get("Duration/String3"),
            "FrameCount":video.get("FrameCount"),
            "FrameRate/String":video.get("FrameRate/String"),
            "wh":f'{video.get("Width")}x{video.get("Height")}',
            "CodecID":video.get("CodecID"),
            "StreamSize/String":video.get("StreamSize/String"),
        }
        daudio = {
            "BitRate/String":audio.get("BitRate/String"),
            "Format/String":audio.get("Format/String"),
            "FrameRate/String":audio.get("FrameRate/String"),
            "SamplingRate/String":audio.get("SamplingRate/String"),
            "StreamSize/String":audio.get("StreamSize/String"),
            "CodecID":audio.get("CodecID"),
        }
        texto = ""
        texto = self._atexto(texto, dgral, "GENERAL")
        texto = self._atexto(texto, dvideo, "VIDEO")
        texto = self._atexto(texto, daudio, "AUDIO")
        return texto

    def _atexto(self, txt:str, dc:dict, titulo:str, num:int=10) -> str:
        txt += f"\n{'-'*num} {titulo} {'-'*num}\n"
        return self.text(dc, txt=txt)
    
    def text(self, dc:dict, sep=" :: ", txt=""):
        """diccionario a texto"""
        for c, v in dc.items():
            txt += f"{c}{sep}{v}\n"
        return txt.rstrip('\n')
    
    def raw(self, tipo:str='general', texto=False, **kw_txt) -> dict|str:
        """tipo: general|video|audio|menu"""
        data = self.DATA_VIDEO.get(tipo)
        return self.text(data, **kw_txt) if texto else data
    
    def peso(self) -> str:
        p = int(self.obten_valor('FileSize', 'general'))
        return self._unidad(p, capital=False)
    
    def resolucion(self) -> str:
        wh = self.wh()
        return f"{wh[0]}x{wh[1]}"
    
    def wh(self) -> tuple[int, int]:
        return int(self.obten_valor('Width','video')),\
                int(self.obten_valor('Height','video'))

    def duracion(self) -> str:
        return self.obten_valor('Duration/String1','video')    
    
    def __str__(self):
        return self.version()
