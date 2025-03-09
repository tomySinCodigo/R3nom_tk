import os, tomllib, json
from os import DirEntry
from pathlib import Path
from typing import Generator, Iterator
from datetime import datetime
import locale


class Funciones:
    def __init__(self):
        self.cargaDc()
        # locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

    def obtenImagenes(self) -> Iterator[str]:
        reno = self.dc.get("reno")
        carpeta = self.miCarpeta(reno["ruta nombres"])
        return carpeta.imagenes(reno["formato imgs"])
    
    def obtenConfigToml(self) -> dict:
        with open("config_reno.toml", "rb") as f:
            return tomllib.load(f)
        
    def cargaDc(self):
        self.dc = self.obtenConfigToml()

    def miCarpeta(self, ruta:str):
        return MiCarpeta(ruta)
    
    def obtenNombres(self, **kw) -> Generator:
        return self.nombresDe(self.obtenImagenes(), **kw)
    
    def nombresDe(self, files:Iterator, stem:bool=True) -> Generator[str,str,str]:
        if isinstance(files, Iterator):
            return (Path(f).stem if stem else Path(f).name for f in files)
        
    def obtenMotores(self) -> list:
        # reno = self.dc.get("reno")["motores"]
        return self.dc.get("reno")["motores"]
    
    def obtenPlantilla(self):
        return self.dc.get("reno")["plantilla"]
    
    def rutaDe(self, rt:str) -> str:
        return Path(rt).as_posix()
    
    def get(self, valor:str, dc='reno'):
        reno = self.dc.get(dc)
        return reno.get(valor)
    
    def getTimeNow(self) -> str:
        locale.setlocale(locale.LC_ALL, '')
        return datetime.now().strftime("%B %d%m%y %A %H:%M:%S")
    
    def makeHistory(self, textold, textnew, rutafolder=""):
        t = self.getTimeNow()
        with open("history RenCores.txt", mode='a') as file:
            file.write(f"{t}|{textold}|{textnew}|{rutafolder}\n")

    

class MiCarpeta:
    def __init__(self, ruta:str):
        self.RUTA = Path(ruta)

    def _contenido(self) -> Generator:
        with os.scandir(self.RUTA) as fs:
            return [r for r in fs]

    def archivos(self) -> Generator[str, str, str]:
        return (Path(f).as_posix() for f in self._contenido() if f.is_file())
    
    def carpetas(self) -> Generator[str, str, str]:
        return (Path(f).as_posix() for f in self._contenido() if f.is_dir())
    
    def nombresDe(self, files:Iterator, stem:bool=True) -> Generator[str,str,str]:
        if isinstance(files, Iterator):
            return (Path(f).stem if stem else Path(f).name for f in files)
        
    def delTipo(self, ext:Iterator=['txt']) -> Generator:
        return (f for f in self.archivos() if Path(f).suffix.strip('.') in ext)
    
    def imagenes(self, ext:list=['jpg', 'png', 'gif']) -> Generator:
        return self.delTipo(ext=ext)
    
    


# TEST
if __name__ == "__main__":
    from pprint import pprint
    fun = Funciones()
    # d = fun.obtenConfigToml()
    # pprint(d)

    # imgs = fun.obtenImagenes()
    # imgs = fun.obtenNombres(stem=False)
    # for img in imgs:
    #     print(img)

    # FECHAS
    print(fun.getTimeNow())

