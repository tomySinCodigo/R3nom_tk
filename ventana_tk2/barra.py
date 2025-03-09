import tkinter as tk
from ventana_tk2.widgets import MiBoton, MiLabelMenu
from ventana_tk2.posicion_ventana import PosicionVentana


class Iconos:
    def __init__(self):
        self.d = {
            "xh":"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAABBElEQVR4nJWSv87BUADFT9vh3ifRl2jSBEuliVUHTTwBW
            8MDmEwYDH0Bg9lLlDSiREJwLSUpNos630DyzT3zbzj/AACANYXhEqLa13UAsCVgS10HIKp9GC4Ba4ofPJuE8/tqm57rjWADmCMpA
            CkAwBzVG8FmtU3Pk3B+B6wZYLjc7Q8ZydMyTui3ekfADAEz9Fu94zJOSPK02x8yGC6hicrAawZJFK9JUt2y9OLU2h+n1v7csvRCU
            kXxml4zSDRRGcDQAKA09PyuejyvKs/fL5IRySjP36/H86o8v6uA0vDLwpY/v+Oy0yHJBf+1KDsdAub4y9hSR1EVtlQ4dOFaiw9X8
            Bp/AjT+XWpNkSsAAAAASUVORK5CYII=""",
            "x":"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAB60lEQVR4nJXSz0vTcRzH8dd3749f00bKoH1bwxYNXJOWs
            0RQdKyc2i+EgV8JZAfty8DFlw7RJTxKl07yxcsYXoYR+w5GQoRJZTYVwuyrGS4RYYwOJojijLHto12qu8+/4Hl4CACgKOGnRBQWR
            TaqaVpMlmURAHRdL6qqqhSL5RHOeTQWiz5jihIeGQgFBuscZ/dn3iy19veFqhJ6XAOA/r6Q2tBwwdt1u3k/l915AMDEiGiozmE9c
            DpctcWb5QBVkHgE/hgAAreavO0dHp/TcRmAsEdEQ4xIeD4z/eVayV/udtdfpDM1Va7DfMEOAHfutZjtkkSZje98dnblM5GwLABAM
            Digdvc0tfUGWy8RY26LxTwHALu7eR8vl9enUotbb6e/LqRSkxqTZVnU9UmNiKNQKEkPH/XO/T4s3QUAi8X8enxsqno+vbKQSr3UZ
            FkWTThhJ1+KRCLDnkbnVb+/se281Uo/t7cz42OvqgFAvu/L2CXJ7r/hPQdByNtsNcOM8+MnXT3XD5wOF9Y31nj607cf8+k1AwBOm
            0952zs8krv+CioqWYuxvNnJOOcTueyvQeB47+N7Y+nDu1UjmXyhAYAJpPISL4qVrDmX3TFzzidYLBYdBXD0l8ZiIhn/TyOhxzXJp
            iqGsdX5j8YfPZPSXv2mMNUAAAAASUVORK5CYII=""",
            "Mh":"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAABuElEQVR4nH2Rv2tTURTHP/e+++7LS4KamlClghEpSIVOC
            kasoIMIKq0/UOgg2L/AgggiCJ3cXHUQR0EHh+ISB1NBXARRwUGhRkszVA1G6kv63st9x6GxdBA/yznLl++HcxARA+Ccuy/rrMl/M
            AzQWqs3b79wbXYuaq/lnOtnKAW+b7D9Xxw7edy7PTcTaCBoNps5wLz/sERj4bW7eHbCXDo/YSZP18yFqSMmzjwePnreBzBKqQhAR
            FY9T1Pdf9C7eX3asomh8jZ19958CmBEpAY4YHcUdaXX7apeLwag14sJw4DW8opkIgAY4NVa7LC+pt3+keSCwIZhAKz7G+MR5iwyC
            GiAoyeupk/mX2Z7qju0y9yGijEeANZapbXaaMiaX1fiTue3rVRKevlTo79rdDryPE2cpElgfVn6+C4bHT+gAW0APbJzuw7zeT156
            pCp1x8Xfq46WVxsyVC5XCgWQgKVMjY+BoASEanuuxxtCTN1ZeacXwwDqQyXzNSZwxp4CnwHPKAPiBIRuXHrQbzwrOFSu1V1Wt/S0
            shw7kX9js2H/l6l1OfNJ+Yf38/+LkmS1ETEiEhxMM0fdObs2ZU5ZrMAAAAASUVORK5CYII=""",
            "M":"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAB60lEQVR4nF2RzWoTYRiFz/vN+01mYjtJkyapaAnVgsVWT
            IUg/ixqRcSNqAu9gF6AuPAGvAJxI4JeRMEutZuiqFTrxir2R6pgmjRN0jbOZH6+10UoiGd5OM/mPCSyyERX4lrj7fPS8PG5TrfRU
            0ql8F/iOEEUxeDDIj+coe8bP/Ds6fye1toRMSAiEBF8P5TK9El989Z5VwFDqc3NRYfh6p9bNXz7+iuuVsf19LkTenKqzJcvTWqlC
            Csf1yJmC0xU6QKAyMY+s8bE6VHrzu1ZB4jQMyFSqgAho5aWvvQAgGu1pQul0tEEsMq+H5jAD1WzsyNRGKMXRjJSALVaBwYiAAAey
            Gbe1HebKOSyaLU6gdZsu65NlqUAAlK2TVpbh3uwUsCTx/PB1WtnOZcfVGIEtt3/IjGGAA2LmYioD8RxYtqtA3+/46ePDDhqeXktf
            PjgRYeIKIqSnuvasrq6lZyaGGUR0QxAeV6a0+mUmp2paDxCJkmM7Db3THbI81K2jes3qiiPjcBL5/sefL8nCy/f+wpkun8CDHou3
            7s7YxPsBUAagFgRgnh757fhOE5QmR7Xnz+tR69er4SddjfO5T1ncmrMLeac+0Rn1v81TtvNd6I1g9lC34eI1kzGCNrtvYvHStGHe
            h1OsYgAAP4C24fO+GQ3w3sAAAAASUVORK5CYII=""",
            "mh":"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAz0lEQVR4nM2QsUoDQRRFz5uZhTW65SKkCboIiT+wZWq/R
            PwAWxvL1IFAuvxB6vyH2qjYBIJNQMbdYmafhS6oxS52nupxeBcuF/4dAlP3xwCIfB0dKKAKQj494vVBYdcTOYZ8LM7U6bqRcUTPe
            rpYTJ1ap+91vlhen5xPRocxxMY6a77/te7u/sVfXc6egXLjfbXXHryv9lBunCSD4uZ2lRanQ0IIOPdztNY9Pm1TSQaF2OxiHt+2A
            SoFAzS/yrfuQGw2dAJgzee0nbMqxAY+AE6vYiv45GBUAAAAAElFTkSuQmCC""",
            "m":"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAA6ElEQVR4nM2NzUrDQBhF78x8yUiE2EqgItNS6EqG0gco
            +BIlT5IHcummuBDcuBHU4gPoths7CCULNYtAk/lxW0LBleBZn3sP8O9geZ6Lvy0URXG8Wr17YzZQ6rBkDKDUEPP5iJO19mo2y5zW
            /SA4R+g+AtDag0gwa62g3a45XeSX08nk/OTzq/KMMb4/CCH4fi/l6/XH983y8ZXa1pUXeiTV2VQCWwBRp9ECGCA+Itleu5KkjMbP
            T2/NUG3rqqqDEIzt686FkKYJ25iykTIaUxxHD3e3L/d13XgijkNY65EkMc+yXjf/Oz/NclEZvTaOQwAAAABJRU5ErkJggg==""",
            "ln":"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAABn0lEQVR4nJWSTUsbURSG33vPnclEJ2ZITFI7LULwo2AaF
            BcFXSiIrkTaXaHQrl248Nf4CwTXpTsRBTdaC7VZ+NGWoERiTBpJdKwzTu693VQJuhCf/eE87zkvO6tva9MU4ETQSkNrDcMwAGg0G
            hdjbibcqVZhpdPwAUCYpsDGemHv8KBUSyZjHd7lte8kYvbbd+MjdsapMZZrAfDwH0FE+HVYqn35vHXcP+DGq5XG1XM3EZueGc27d
            tdSqPfrDIz7QRB4l38DobVGPG5Hs9lndk9PosMyIiyV6bIA4HvhYLJcPvetqCleuClrsG8AAgCUkioIQhW2pPJvbpSUEkScF3aLX
            ws/jsqnp3U/l+tNLCwmJwTuQZxBSqXCUMr3H6befProYHV9s7j77WeJMWbx+wOP8WCDVBpEnBsG0cry2na7ktbaFwDAOfFIxOCGI
            G6ZJiciSKlUfjg72p12hm5Dx6JJCMYYmk3vuliseCSIqpXGVUuFDABG8q82XufDu7Oe/TkJhJQS/YMvU7NzQPvjOjstasKfd1jud
            7sye2o1/gH4QcSwh0lI6gAAAABJRU5ErkJggg==""",
            "lh":"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAABcElEQVR4nJWSsWtUQRCHv327e/viu7yIl5yGS2GhKAYuN
            kHE7sAghPwBNpJ0lnYimNrKKrVEBLERLEwKT9BWIhamU4gkkESOuyAeZ+K+9zZjcwbCiZCvmWFgmN9vZpBBDv8mWZZdFxEjIuV+N
            Abg/sMn/tOHjyE5U432f/ws0uqoe/l80VprW0qpAujRR4mITF27u7++9iqHCxpaAWq223szNJzEK0AH0EABiAGYqI2pL+58lI7XV
            Pe705WJs6IVNN+tz21tbHN6JOFK/RKTl89hAPK8wPsM73O8/y15CKpUsmr52Wr37cr7fG+vLRfrV6Ovn5dPRQygKfJA79eBvHj6I
            O10mpXHS4sjzrkYiP/R8H/MYClgrKacDKnb84+OSQIiA2CtwbkSzlmci5XVmizLZeHObNq4MXVk+mjC9k5bvN88bG8aBa2wuxFsE
            Jhp1F/TqA+u9dbNaT02DP3DkVZHbTmJFXBPKfXtmOKTvsYfeOLXP6vJN2YAAAAASUVORK5CYII=""",
            "kh":"""iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAACNElEQVR4nGVRTUhUYRQ9933fG2ecn5ejZCJRLlqEWwmxg
            lq0imiRDzcqtR1ahBSitoh+UCFqEwgitMhAkKgIW1hIUC5KqbZCaGZmkUzoqDPz3vveaaGjQ53V5Z57LvecK9iGkISIsK6u9nY8W
            Xk2lUyuAsB6LlezmduaWFn5dZ2kiAgAEADEdV2VyWQSzcebesafDufIbHZyaiycnBoLyWx2/NlwrrmlqTeTySRc11UABABUJGIDQ
            MuNW1dJ/v44/PDuIwBdALqGRgbGyPXZm3euEcCJigobAJSFPSjfK+aBmnxf98ARkveVVvd6uwerAMvOb+XXAHjk9rAFIBwdfawAz
            E1Pz460tp07tM9JDTU27o+bwNTX1lYHgFBEdOnEcpQ3jpbVycMNByfIzc89fZc3ABzbsaU0AAXAaK1Paq26dMRe9AqFtOOkLN83K
            haLFQFjKaWgtdbForedrNYaABraOy8sbPnznJt/y8UfM3zz7kkw8+ml/21l1ix8fx8UzFd2XGz9AqBBa41SOGJZlkR0BLYdMY6Tx
            GD/g1dnTre9dpyUZUwIZSkI9nzupkqQIUKQhOf5aO90dbo6rYMgKPEgSpmWCXcXkLBtG5c6rojvBWJZ/40AAPSeAqExIRmSJOl7X
            n5paRkkGYakMSFBhP8KRUSiURWXykRMiwimP7w4VSLiiZiOqjhEJFryKDvvkPr6A+ejsYoegqs01FVpxwaAP9k1X5QEAqkp5Iv9y
            8s/nwPgX8AA9jm840XpAAAAAElFTkSuQmCC""",
            "k":"""iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAACYUlEQVR4nFWSS0hUcRTGf//HvbdSR8eZHhY9tk0QkrsgR
            igIhDZFLYJatBEswRZKm3AhuGgV5EoXSS4Sw6BNkFDOOiwkiFZtekHNmI8ZZ+6987/3tGgMO3A2h+/HOd/hQ0TaRUQVi0WrtQbwg
            CyQaXUW8LTWFItFKyJtIpJRACsrK15fX59VSrnTvSen9ufzF7uymQrAxvpWvlypvPqw+umOiNjp6Wk3ODjYBFAi47pQKHQPXLowt
            VSar4o0vy2+mIkWX8xEIs1vS6X56sClC1OFQqF7YeGqARSACQIf4NzE5JiI1N+O3ht6CtwAbozeG3oqUn87MTkmwLmW1mgAEcFaG
            zfqjU1Ig9nHC/kg8OeCwJ+bfbyQhzRo1Bub1tpYRACwtMo5F0ZRbECnvuetR1H8EMD3vHXQ+SiKjXMu9H0PAGWtxVp77MrVgecPH
            02cCcNGvLVVSyrl3/s836Ozs6OeybSbPXv2+iPD998vPnt52Tn3xQKEYegZo3tynVn1eWPTO37iaHB3ePz1l6/febf66vyPHz/TI
            wcPK2N0TxiGnrUW3bpUQEUOhzFGtmvbDI/cSmq1ehKGEUopcThARX+1/AMRRAGkaYrv+1y/dtsYpU0rFP9pdj9HEHFx3JTEuTRJE
            lWt1rar1RpJkqSJc2kcNzUibmfjDmi1tt1tfo86eKjpte9rY+nN/FmArkxGW2t0m9+D1rZ7h1HLy8u2v7/fnu49dTOXy46JpBVJx
            eYP5HyAyq+1WGnllNL5tbX1Bx9WPz4plUqOcrncsctHDugEunaFvKs1ywForSmXyx1/ABw8E3O23rSdAAAAAElFTkSuQmCC""",
        }

    def get(self, nom:str) -> str:
        return self.d.get(nom)


class FrameBotones(tk.Frame):
    def __init__(
        self, parent, bgh='gray10',
        bghx='#F92672', bga='#101010',
        *args, **kw
    ):
        super().__init__(master=parent, *args, **kw)
        self.bgh = bgh
        self.bga = bga
        self.bghx = bghx
        self._wg_Framebotones()

    def _wg_Framebotones(self):
        self.columnconfigure(0, weight=1)

        ic = Iconos()
        self.ic_m = tk.PhotoImage(data=ic.get("m"))
        self.ic_mx = tk.PhotoImage(data=ic.get("M"))

        self.bt_top = MiBoton(self)
        self.bt_top.grid(row=0, column=0, sticky='wens', ipadx=0)
        self.bt_top.setIcon(data=ic.get("kh"))
        # self.bt_top.setIconHover(data=ic.get("kh"))
        self.bt_izq = MiBoton(self, width=18)
        self.bt_izq.grid(row=0, column=1, sticky='wens')
        self.bt_izq.setIcon(data=ic.get("ln"))
        self.bt_izq.setIconHover(data=ic.get("lh"))

        self.bt_min = MiBoton(self)
        self.bt_min.grid(row=0, column=2, sticky='wens')
        self.bt_min.setIcon(data=ic.get("m"))
        self.bt_min.setIconHover(data=ic.get("mh"))
        self.bt_fw = MiBoton(self, image=self.ic_mx)
        self.bt_fw.grid(row=0, column=3, sticky='wens')
        self.bt_fw.setIcon(data=ic.get("M"))
        self.bt_fw.setIconHover(data=ic.get("Mh"))
        self.bt_x = MiBoton(self, bgh="red")
        self.bt_x.setIcon(data=ic.get("x"))
        self.bt_x.setIconHover(data=ic.get("xh"))
        self.bt_x.grid(row=0, column=4, sticky='wens')


class Barra(tk.Frame):
    def __init__(self, parent=None, *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self._widget_Barra()
    
    def _widget_Barra(self):
        self.estado_max = False
        self.POS_IZ = True
        self.TOP = True
        self.ic = Iconos()

        self.columnconfigure(1, weight=1)
        self.lb_menu = MiLabelMenu(self)
        self.lb_menu.grid(row=0, column=0)

        self.text_titulo = tk.Text(
            self, height=1, padx=6, font=("Consolas", 8, "bold"),
            bg='#303030', fg="#E5E5E5", relief="flat",
            selectbackground='#202020',
            selectforeground='orange',
        )
        self.text_titulo.grid(row=0, column=1, sticky='wens')
        self.text_titulo.config(state='disabled')

        self.fm_bts = FrameBotones(self)
        self.fm_bts.grid(row=0, column=3, sticky='we')
        self.fm_bts.bt_x.config(command=self.cerrar)
        self.fm_bts.bt_fw.config(command=self.maximiza)
        self.fm_bts.bt_izq.config(command=self.alternaLado)
        self.fm_bts.bt_top.config(command=self.ontop)

        self.parent.bind("<ButtonPress-3>", self.startMove)
        self.parent.bind("<ButtonRelease-1>", self.stopMove)
        self.parent.bind("<B3-Motion>", self.onMotion)
        self.M1_X = 0
        self.M1_Y = 0

        
    def setSize(self, w=600, h=16, **kw):
        self.pv = PosicionVentana(self.parent, w, h)
        # self.pv.cnf(tam=1/2)
        self.pv.cnf(**kw)
        self.pv.centrar()

    def cerrar(self, e=None):
        self.parent.destroy()

    def maximiza(self, e=None):
        if self.estado_max:
            self.parent.wm_state('normal')
            self.estado_max = False
        else:
            self.parent.wm_state('zoomed')
            self.estado_max = True

    def alternaLado(self):
        self.pv.izq() if self.POS_IZ else self.pv.der()
        self.POS_IZ = not self.POS_IZ

    def cnf(self, **kw):
        self.pv.cnf(**kw)

    def menuItem(self, nom, cmd):
        """asigna items al menu de la barra"""
        self.lb_menu.cmd(texto=nom, metodo=cmd)

    def msg(self, texto, tag='_tg', fg=None, bg=None, **kwargs):
        self.text_titulo.config(state='normal')
        self.text_titulo.insert('end', texto, (texto, tag))
        if fg:
            self.text_titulo.tag_config(tag, foreground=fg, **kwargs)
        if bg:
            self.text_titulo.tag_config(tag, background=bg, **kwargs)
        self.text_titulo.config(state='disabled')

    def setIconMenu(self, **kw):
        """image, **kw:cnf label menu"""
        self.lb_menu.cnfLabelMenu(**kw)

    def _top(self, b=True):
        self.parent.attributes('-topmost', b)

    def ontop(self):
        if self.TOP:
            self._top()
            self.fm_bts.bt_top.setIcon(data=self.ic.get("k"))
        else:
            self._top(b=False)
            self.fm_bts.bt_top.setIcon(data=self.ic.get("kh"))
        self.TOP = not self.TOP

    def startMove(self, e):
        """save mouse position"""
        self.M1_X, self.M1_Y = e.x, e.y

    def stopMove(self, e):
        """reset values"""
        self.M1_X, self.M1_Y = 0, 0

    def onMotion(self, e):
        """move window when is dragged"""
        x = self.parent.winfo_x() + (e.x - self.M1_X)
        y = self.parent.winfo_y() + (e.y - self.M1_Y)
        self.parent.geometry(f"+{x}+{y}")

    def setBg(self, color:str):
        self.config(bg=color)
        self.fm_bts.config(bg=color)
        self.fm_bts.bt_top.setBg(color)
        self.fm_bts.bt_izq.setBg(color)
        self.fm_bts.bt_min.setBg(color)
        self.fm_bts.bt_fw.setBg(color)
        self.fm_bts.bt_x.setBg(color)
        self.text_titulo.config(bg=color)





if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry("400x200")

    vn.mainloop()