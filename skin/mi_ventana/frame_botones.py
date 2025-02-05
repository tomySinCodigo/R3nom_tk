import tkinter as tk
import tomllib


class IconoTk():
    def __init__(self):
        self.NORMAL = None
        self.HOVER = None

    def normal(self, **kw):
        self.NORMAL = tk.PhotoImage(**kw)

    def hover(self, **kw):
        self.HOVER = tk.PhotoImage(**kw)
    
    def asigna(self, **kw):
        return tk.PhotoImage(**kw)
    

class Boton(tk.Button):
    def __init__(self, parent=None, bg='#303030', bgh='#272822', *args, **kw):
        super(Boton, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self.bg = bg
        self.bgh = bgh
        self.icono = IconoTk()
        self._cnf()

    def on_enter(self, e):
        self['bg'] = self.bgh
        self.config(image=self.icono.HOVER)
    
    def on_leave(self, e):
        self['bg'] = self.bg
        self.config(image=self.icono.NORMAL)

    def asigna_icono(self, **ico):
        self.icono.normal(**ico)
        self.icon = self.icono.asigna(**ico)
        self.config(image=self.icon)
    
    def icono_hover(self, **ico):
        self.icono.hover(**ico)

    def _cnf(self):
        d = {
            'relief':'flat',
            'bg':self.bg
        }
        self.config(**d)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def ico(self, nom:str):
        self.icono.ico(nom)


class FrameBotones(tk.Frame):
    def __init__(
        self, parent, bgh='#101010', bghx='#F92672', bga='#101010',
        *args, **kw
    ):
        super().__init__(master=parent, *args, **kw)
        self.bgh = bgh
        self.bga = bga
        self.bghx = bghx
        self.cnf = self.lee_toml()
        self._wg_Framebotones()

    def _wg_Framebotones(self):
        d = {'bgh':self.bgh, 'activebackground':self.bga}

        self.bt_top = self.crea_botonDos(
            'lock.png',
            bg=self.bgh,
            activebackground=self.bga 
        )
        self.bt_top.grid(row=0, column=0, sticky='e')
        self.bt_izq = self.crea_boton('izq2n.png', 'izq2h.png',**d)
        self.bt_izq.grid(row=0, column=1, sticky='e')
        self.bt_min = self.crea_boton('minn.png', 'minh.png', **d)
        self.bt_min.grid(row=0, column=2, sticky='e')
        self.bt_fw = self.crea_boton('f2n.png', 'f2h.png', **d)
        self.bt_fw.grid(row=0, column=3, sticky='e')
        self.bt_x = self.crea_boton('xn.png', 'xh.png', **d)
        self.bt_x.grid(row=0, column=4, sticky='e')
        self.bt_x.bgh = '#F92672'

    def lee_toml(self):
        with open('skin/mi_ventana/config.toml', "rb") as f:
            return tomllib.load(f)

    def crea_boton(self, ico, icoh, **kw):
        ruta = self.cnf.get('ico')['ruta']
        bt = Boton(self, **kw)
        bt.asigna_icono(file=f"{ruta}/{ico}")
        bt.icono_hover(file=f"{ruta}/{icoh}")
        bt.bgh = self.bgh
        return bt
    
    def crea_botonDos(self, ico, **kw):
        ruta = self.cnf.get('ico')['ruta']
        self.icc = tk.PhotoImage(file=f"{ruta}/{ico}")
        bt = tk.Button(self, image=self.icc, relief='flat', **kw)
        return bt
    
    def get_ruta(self):
        return self.cnf.get('ico')['ruta']