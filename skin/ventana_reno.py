from skin.oskin import OSkin
from skin.mi_ventana.mi_ventana_dnd import MiVentana


class VentanaReno(MiVentana):
    def __init__(self, bg:str, bg_bar:str, **kw):
        super().__init__(bg, **kw)
        self._iniciaVentanaReno(bg, bg_bar)


    def _iniciaVentanaReno(self, bg, bg_bar='yellow'):
        self.bg(color=bg)
        self.bgBar(bgcolor=bg_bar, **dict(bg=bg_bar))
        self.ladoTam(1/2)

        self.osk = OSkin(self.nbk.pag1)
        self.osk.grid(row=0, column=0, sticky='wens')
        self.nbk.pag1.rowconfigure(0, weight=1)
        self.nbk.pag1.columnconfigure(0, weight=1)




if __name__ == '__main__':
    app = VentanaReno()
    app.geometry("650x350")
    app.mainloop()