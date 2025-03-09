from pathlib import Path
from ventana_tk2 import VentanaTk
from skin_ren import SkinRen
from funciones import Funciones
from corex import Corex, MiMediaInfo


class VentanaRen(VentanaTk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.__configVentanaRen()

    def __configVentanaRen(self):
        ico = """iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABb0lEQVR4nKWTMUgCYRiGH0XFxKLlAiPSgoiCqAhqc
        alBDhtqcbkadBJacgmCIxoiamxoaaqpxSU3N4cMwjzIRTfRRSOhQQTlgq7pzi7LLnzhG/7/fb+Xl//7fpuqhDUGgAMgKj9xm270F
        UqiwKW8jNfjMN3b9ASlcpPFSJZCMsjc9IhJVG90iMo5AG5OV/EJboOzW4npE9xcHC6RUVqkH15MnCUDgNFhF+srXmqvbdT3j/8bl
        MpNMkqL8bEhXM5umyWDUrmJuJdHEgUioQkT5/guXoxkfzQ5jk9xEJvF5bTj36oAUE0Feg30KVzfVYifFLk6mie2HTBpqqnuucdAh
        94UPyni93nYWBszuL4JvmJnc5LaaxtxL2/aj68J+j6iy2lnf3cGSRRInD9Tb3SMBHqKP6fg9Tg4SywAEJVz1BsdqqlAN4WqhDVJF
        DTAqOP4lNZ6FDVVCRtVSAYNXhIF7e0+pKlKWLMN+hstb+Jv+AQip4awpc/mqgAAAABJRU5ErkJggg=="""
        self.setIconData(ico)
        self.bar.setBg(color='gray20')

        self.wg = SkinRen(self)
        self.wg.grid(row=1, column=0, sticky='wens')
        self.addGrip() 
        self.setBg('gray0') # esto ,luego de agregar el grip
        self.rowconfigure(1, weight=1)
        # self.columnconfigure(0, weight=1)
        self._setCommands()

    def _setCommands(self):
        self.fun = Funciones()
        self.wg.bt_recarga.config(command=self._recargaValores)
        self.wg.cmb_tags.cmdSelected(self._seleccionaTag)
        self.wg.tree.cmdSelect(self._seleccionaItemTree)
        self.wg.bt_previa.config(command=self.genPrevia)
        self.wg.bt_rename.config(command=self.renombrarArchivos)
        self.wg.bt_rename.disabled()
        self.wg.bt_cleartags.config(command=self.wg.en_tags.clear)
        self.wg.bt_coresinfo.config(command=self.muestraInfoCores)
        self._recargaValores()

    def _recargaNombres(self):
        noms = list(self.fun.obtenNombres())
        self.wg.cmb_tags.items = noms
        self.wg.tex.msgNum("CONFIG: ")
        self.wg.tex.msgNum(f"{len(noms)} tags cargados.\n", 1)

    def _recargaCores(self):
        cores = self.fun.obtenMotores()
        self.wg.cmb_cores.items = cores
        self.wg.tex.msgNum("CONFIG: ")
        self.wg.tex.msgNum(f"{len(cores)} cores cargados.\n", 1)
        self.wg.cmb_cores.currentIndex = self.fun.get("motor elegido")

    def _recargaValores(self):
        self._recargaNombres()
        self._recargaCores()
        self._recargaPlantilla()

    def _recargaPlantilla(self):
        p = self.fun.obtenPlantilla()
        self.wg.en_plantilla.setText(p)

    def _seleccionaTag(self, e=None):
        item = self.wg.cmb_tags.currentItem
        sep = self.fun.get('sep nombres')
        texto = self.wg.en_tags.text()
        if texto:
            if sep in texto:
                lista = texto.split(sep)
                if not item in lista:
                    texto += f"{sep}{item}"
                    self.wg.en_tags.setText(texto)
            else:
                texto += f"{sep}{item}"
                self.wg.en_tags.setText(texto)
        else:
            self.wg.en_tags.setText(item)

    def getDrop(self, e):
        archivos = super().getDrop(e)
        self.wg.tree.setItems(archivos)
        self.wg.tree.setCurrentIndex(1)
        # file = self.wg.tree.currentItem()
        self.wg.tex.msg(
            texto=" FILE ", tag="_file", bog='gray10', fog='lightgreen',
            font="Consolas 8 bold"
        )
        self.wg.tex.msg(" ")
        self.wg.tex.msgNum(archivos[0]+"\n", i=7)

    def _seleccionaItemTree(self, e=None):
        data = self.wg.tree.currentItem
        if data: # por si se selecciona el folder
            self.wg.en_newname.setText(data.get('stem'))
        # print(data)

    def genPrevia(self):
        try:
            core = self.wg.cmb_cores.currentItem
            tags = self.wg.en_tags.text()
            cmd = self.wg.en_plantilla.text()
            data_item = self.wg.tree.currentItem
            video = data_item.get('r')

            cx = Corex(
                rvideo=video, core=core, tags=tags, cmd=cmd
            )
            sufijo = cx.getTranslate()
            nom = self.wg.en_newname.text().strip().lower()
            new = f"{nom} {sufijo}"
            self.wg.en_newname.setText(new)

            self.wg.tex.msgNum(nom, i=1)
            self.wg.tex.msgNum(" ")
            self.wg.tex.msgNum(sufijo, i=3)
            self.wg.tex.msgNum(data_item.get('suffix')+"\n", i=1)
            self.wg.bt_rename.enable()
        except Exception as err:
            self.wg.tex.error(str(err)+"\n")

    def renombrarArchivos(self):
        try:
            data_item = self.wg.tree.currentItem
            if data_item:
                video = data_item.get('r')
                _ = Path(video)
                new_stem = self.wg.en_newname.text()
                if new_stem and data_item.get('stem')!=new_stem: 
                    oldpath = Path(video)
                    newpath = _.with_stem(new_stem)
                    # oldpath.rename(newpath)
                    self.fun.makeHistory(
                        textold=oldpath.name, textnew=newpath.name,
                        rutafolder=_.parent.as_posix()
                    )
                    self.wg.tex.msg(
                        texto=" RENAME ", tag="_file", bog='gray10', fog='lightgreen',
                        font="Consolas 8 bold"
                    )
                    self.wg.tex.msg(" ")
                    self.wg.tex.msgNum("Archivo renombrado, con exito.\n", i=0)
                    self.wg.bt_rename.disabled()
            else:
                self.wg.tex.msgNum("item no seleccionado", 8)
        except IndexError as ierr:
            self.wg.tex.error(f'TREEVIEW: {ierr}\n')
        except Exception as err:
            self.wg.tex.error(str(err)+"\n")

    def muestraInfoCores(self):
        core = self.wg.cmb_cores.currentItem.lower()
        print('core :: ', core)
        self.wg.tex.msgNum("iNFO CORES:", 1)
        match core:
            case "mediainfo":
                self._doc_mediainfo()
            case "ffmpeg":
                self._doc_ffmpeg()
            case "exiftool":
                self._doc_exiftool()
            case "mp4info":
                self._doc_mp4info()
            case _:
                self._doc_ffmpeg()


    def _doc_mediainfo(self):
        # res = self.wg.tree.getItems()
        self.msgn(' MEDIAINFO\n', 3)
        self.msgn('VIDEO: ')
        self.msgn('bitrate, duration, codec, height, width, t\n', 11)
        self.msgn('AUDIO: ')
        self.msgn('bitrate, codec\n', 11)
        self.msgn('GENERAL: ')
        self.msgn('bitrate, size, filesize, format, duration\n', 11)

    def _doc_ffmpeg(self):
        self.msgn(' FFMPEG\n', 3)
        self.msgn('VIDEO: ')
        self.msgn('bitratev, duration, codecv, height, width\n', 11)
        self.msgn('AUDIO: ')
        self.msgn('bitratea, codeca\n', 11)
        self.msgn('GENERAL: ')
        self.msgn('bitrateg, size, durationts, duraciong\n', 11)

    def _doc_exiftool(self):
        self.msgn(' EXIFTOOL\n', 3)
        self.msgn('GENERAL: ')
        self.msgn('bitrateg|bitratev, size, size, filesize, codecg, duraciong, height, width\n', 11)
        self.msgn('VIDEO: ')
        self.msgn('duracion, codec, alto, ancho\n', 11)

    def _doc_mp4info(self):
        self.msgn(' MP4INFO\n', 3)
        self.msgn('VIDEO: ')
        self.msgn('duracion, bitratev, codecv, alto, ancho\n',11)
        self.msgn('AUDIO: ')
        self.msgn('codeca, bitratea\n',11)

    def msg(self, texto, **kw):
        self.wg.tex.msg(texto, **kw)

    def msgn(self, texto, i=0, **kw):
        self.wg.tex.msgNum(texto, i, **kw)


if __name__ == '__main__':
    ventana = VentanaRen()
    ventana.geometry('780x400')
    ventana.mainloop()