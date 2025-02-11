from pathlib import Path
from skin.oskin import OSkin
from skin.mi_ventana.mi_ventana_dnd import MiVentana
from fren.funciones import Funciones
from cores.corex import CoreX


class VentanaReno(MiVentana):
    def __init__(self, bg:str, bg_bar:str, **kw):
        super().__init__(bg, **kw)
        self._iniciaVentanaReno(bg, bg_bar)


    def _iniciaVentanaReno(self, bg, bg_bar='yellow'):
        self.bg(color=bg)
        self.bgBar(bgcolor=bg_bar, **dict(bg=bg_bar))
        self.ladoTam(1/2)

        self.osk = OSkin(self.nbk.pag1, bg=bg)
        self.osk.grid(row=0, column=0, sticky='wens')
        self.nbk.pag1.rowconfigure(0, weight=1)
        self.nbk.pag1.columnconfigure(0, weight=1)

        self.NOMBRES = []

        self.fun = Funciones()
        self.osk.bt_recarga.config(command=self.cargaNombres)
        self.osk.cmb_nombres.metodo(self.seleccionaNombre)
        self.metodoDrop(self.dropArchivo)
        self.osk.bt_previa.config(command=self.aplicaPrevia)
        self.RUTAVIDEO = None

        self.setLabelCmd("toggle scroll", self.osk.tex.toggleScroll)

    def cargaNombres(self):
        imgs = [i for i in self.fun.obtenNombres()]
        self.osk.cmb_nombres.items = imgs
        ruta = self.get("ruta nombres")
        self.msgNum(f"FOLDER: {ruta}\t", i=1)
        self.msgNum(f"{len(imgs)} imagenes cargados.\n")

        self.cargaPlantilla()
        self.cargaCores()
    
    def msg(self, texto, **kw):
        """texto, i[0-8] tag, fg, bg"""
        self.osk.msg(texto, **kw)

    def msgNum(self, texto, i=0, **kw):
        """texto, i[0-8], kw[tag, fg, bg]"""
        self.osk.msgNum(texto, i, **kw)

    def get(self, nom:str, d='reno'):
        return self.fun.get(nom, d)
    
    def cargaPlantilla(self):
        plantilla = self.get("plantilla")
        self.osk.PLANTILLA.set(plantilla)

    def cargaCores(self):
        self.osk.cmb_core.items = self.get("motores")
        self.osk.cmb_core.indice = self.get("motor elegido")

    def seleccionaNombre(self, e=None):
        nombre = self.osk.cmb_nombres.elegido
        if nombre not in self.NOMBRES:
            self.NOMBRES.append(nombre)
        sep = self.get("sep nombres")
        self.osk.NOMBRE.set(sep.join(self.NOMBRES))

    def dropArchivo(self, evento):
        archivos = self._fix_rutas(evento.data)
        for archivo in archivos:
            self.msgNum(f"{archivo}\n")
        self.osk.tree.asigna_ruta(archivos)
        video = Path(archivos[0])
        self.RUTAVIDEO = video.as_posix()
        # self.msg(f"{video.name}\n")

    def aplicaPrevia(self):
        core = self.osk.cmb_core.elegido
        plantilla = self.osk.PLANTILLA.get()
        # self.msgNum(f"{core} - {plantilla}\n")
        plantilla = self.getNombre(plantilla=plantilla)
        
        self.NEWRUTAVIDEO = None
        if self.RUTAVIDEO and Path(self.RUTAVIDEO).exists():
            corex = CoreX(plantilla, self.RUTAVIDEO)
            match core:
                case "MediaInfo":
                    salida = corex.useMediaInfo()
                case "FFmpeg":
                    salida = corex.useFFmpeg()
                case _:
                    salida = ""
            # print(corex.useFFmpeg())
            # self.osk.msgNum(texto=salida+"\n", i=4)
            video = Path(self.RUTAVIDEO)
            self.NEWRUTAVIDEO = f"{video.parent}/{video.stem} {salida}{video.suffix}"
            self.msgNum(f"{self.NEWRUTAVIDEO}\n")
            self.msgNum(f"{Path(self.NEWRUTAVIDEO).name}\n", i=6)
            self.osk.NEWNOMBRE.set(Path(self.NEWRUTAVIDEO).name)

    def getNombre(self, plantilla:str) -> str:
        """comando a nombre"""
        nombre = self.osk.NOMBRE.get().strip()
        # self.msg(nombre+"\n")
        cmd = " $modelos$"
        if cmd in plantilla:
            if nombre:
                plantilla = plantilla.replace(cmd, f" {nombre}")
            else:
                plantilla = plantilla.replace(cmd, "")
        return plantilla


        





if __name__ == '__main__':
    app = VentanaReno(bg='gray40', bg_bar="#202022")
    app.geometry("650x350")
    app.mainloop()