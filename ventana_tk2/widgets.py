import tkinter as tk


class Iconos:
    def __init__(self):
        self.d = {
            "menu":"""iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAA3ElEQVR4nKWSIVIDQRBF389uEAgcFhGBRuG5QS4Bh0
            JxhFRxADwKjUoRiUeQZB8iM1WLmGKp/ap//e6enu4PM5EaqMsx/wMm2c99/DSBukgyqA/ANXAA+kZ+1d6TPKoL1B5A3Tkdu1LT98
            BQuj8BN8AeWDYmqNpb4UMjbzrGVzgv/5P2Nap2SPIFpyV2SY7qBrgDvoGzRoOqvSRZq9142yvgYuLkqxqMl3gPXBa+aBRW7XPE5y
            FqkqiugSvgCHSN/Kp9JNmoGRtp+w8jbUvNLyM9A7dMM9Jr4fN38APLJ7I/zrX5CQAAAABJRU5ErkJggg==""",
            "menu2":"""iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAKUlEQVR4nGP8//8/AzmAiSxdlGhkQWIT62ZGqtnIS
            IrGUT8SaeMg9yMAFgMGKNHM5FQAAAAASUVORK5CYII="""
        }
    
    def get(self, nom:str) -> str:
        return self.d.get(nom)

class IconoTk():
    def __init__(self):
        self.NORMAL = None
        self.HOVER = None

    def normal(self, **kw):
        self.NORMAL = tk.PhotoImage(**kw)

    def hover(self, **kw):
        self.HOVER = tk.PhotoImage(**kw)
    
    def set(self, **kw):
        return tk.PhotoImage(**kw)
    

class MiBoton(tk.Button):
    def __init__(
        self, parent=None,
        bg='gray30', bgh='black', bga='#4C5043',
        fg='#CBD3C4', fgh='#F0EAD6', fga='white',
        *args, **kw
    ):
        super(MiBoton, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self.bg = bg
        self.bgh = bgh
        self.bga = bga
        self.fg = fg
        self.fgh = fgh
        self.fga = fga

        self._cnf()
        self.icono = IconoTk()

    def on_enter(self, e):
        self['bg'] = self.bgh
        self['fg'] = self.fgh
        self.config(image=self.icono.HOVER)
    
    def on_leave(self, e):
        self['bg'] = self.bg
        self['fg'] = self.fg
        self.config(image=self.icono.NORMAL)

    def setIcon(self, **ico):
        self.icono.normal(**ico)
        self.icon = self.icono.set(**ico)
        self.config(image=self.icon)
    
    def setIconHover(self, **ico):
        self.icono.hover(**ico)

    def _cnf(self):
        self.recargaConfig()
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def recargaConfig(self):
        d = {
            'relief':'flat',
            'fg':self.fg,
            'bg':self.bg,
            'activeforeground':self.fga,
            'activebackground':self.bga,
            'font':'Consolas 9 bold'
            # 'highlightcolor':self.fgh,
            # 'highlightbackground':self.bgh
        }
        self.config(**d)

    def ico(self, nom:str):
        self.icono.ico(nom)

    def setBg(self, color:str):
        self.config(bg=color)
        self.bg = color
        self.recargaConfig()

class MiLabelMenu(tk.Label):
    def __init__(self, parent=None, *args, **kw):
        # icono=None,
        # titulo='PROGRAMA', compound='left',
        # font="Consolas 8 bold", bg="gray10", fg="azure",
        super(MiLabelMenu, self).__init__(
            master=parent, *args, **kw
        )
        self.parent = parent
        self._config_MiLabelMenu()

    def _config_MiLabelMenu(self):
        ic = Iconos()
        self.menu = tk.Menu(
            self, tearoff=False
        )
        self.icono = tk.PhotoImage(data=ic.get("menu2"))
        cnf_menu = dict(
            text=" PROGRAMA", compound="left",
            font="Consolas 8 bold", bg="gray10", fg="azure",
            image=self.icono, anchor="se"
        )
        self.cnfLabelMenu(**cnf_menu)
        cnf = dict(
            activebackground="black",
            font="Consolas 8 bold"
        )
        self.cnfMenu(**cnf)
        self.bind("<Button-1>", self.menuAction)

    def cnfMenu(self, **kw):
        self.menu.config(**kw)

    def cnfLabelMenu(self, **kw):
        self.config(**kw)

    def cmd(self, texto:str, metodo):
        self.menu.add_command(label=texto, command=metodo)

    def menuAction(self, e):
        # COORDENADAS DE LA VENTANA
        wx, wy = self.winfo_rootx(), self.winfo_rooty()
        # ancho y alto de label
        lb = e.widget
        lbw, lbh = lb.winfo_width(), lb.winfo_height()
        self.menu.tk_popup(wx, wy+lbh)


class MiGrip(tk.Frame):
    def __init__(self, parent, bg="lightblue", cursor="bottom_right_corner", w=10, h=15):
        super().__init__(master=parent, bg=bg, cursor=cursor, width=w, height=h)
        self.parent = parent

    # Función para redimensionar la ventana
    def start_resize(self, event):
        self.start_x = event.x_root
        self.start_y = event.y_root
        self.start_width = self.parent.winfo_width()
        self.start_height = self.parent.winfo_height()

    def perform_resize(self, event):
        delta_x = event.x_root - self.start_x
        delta_y = event.y_root - self.start_y
        new_width = max(self.start_width + delta_x, 100)  # Ancho mínimo
        new_height = max(self.start_height + delta_y, 100)  # Alto mínimo
        self.parent.geometry(f"{new_width}x{new_height}")



if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry("450x200")

    # wg = MiBoton(vn, width=60, text="\u2715", compound='left')
    # wg = MiBoton(vn, width=60, text="╳", compound='left')
    # wg = MiBoton(vn, width=60, text="❑ ▼ ■ x", compound='bottom', font="Consolas 12 bold")
    # wg.setIcon(file="otros/icons8-toggle-off-32.png")
    # wg.setIconHover(file="otros/icons8-toggle-on-32.png")
    # wg.pack()
    # tk.Button()
    def uno():
        print("uno")

    lm = MiLabelMenu(vn, text=" MI PROGRAMA")
    lm.cmd("uno", uno)
    lm.pack()

    vn.mainloop()