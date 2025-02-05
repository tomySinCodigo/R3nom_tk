import tkinter as tk
import tomllib
from mi_ventana.barra import Barra
from mi_ventana.frame_drag import FrameDrag
from mi_ventana.drag_para import DragPara


class MiVentana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("600x160")
        
        self.bar = Barra(self)
        self.bar.grid(row=0, column=0, sticky="wens")
        
        self.fm = FrameDrag(self, bg='#201620')
        # fm = tk.Text(self, bg='skyblue')
        self.fm.grid(row=1, column=0, sticky='wens')
        self.overrideredirect(1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.drag = DragPara(self)
        self.bar.bind('<Enter>', self.barra_in)
        self.bar.bind('<Leave>', self.barra_out)
        self.barra_color(bg='#303030')
        self.config(bg='red')

    def barra_in(self, e):
        #~ print("encima")
        self.bind('<ButtonPress-3>', self.drag.posicion_relativa)
        self.bind('<ButtonRelease-1>', self.drag.drag_unbind)
        # self.bind('<ButtonRelease-3>', self.nobind)

    def barra_out(self, e):
        #~ print("fuera")
        self.unbind('<Motion>')

    def nobind(self, e):
        self.unbind('<Motion>')
        self.unbind('<ButtonPress-1>')
        self.unbind('<ButtonRelease-3>')

    def bg(self, color='#606060'):
        self.fm.config(bg=color)
        self.fm.grip_se.config(bg=color)
        self.fm.grip_sw.config(bg=color)

    def barra_color(self, bg='blue'):
        self.bar.config(bg=bg)
        self.bar.text_titulo.config(bg=bg)
        self.bar.bts_base.bt_izq.config(bg=bg)
        self.bar.bts_base.bt_izq.bg = bg
        self.bar.bts_base.bt_min.config(bg=bg)
        self.bar.bts_base.bt_min.bg = bg
        self.bar.bts_base.bt_fw.config(bg=bg)
        self.bar.bts_base.bt_fw.bg = bg
        self.bar.bts_base.bt_x.config(bg=bg)
        self.bar.bts_base.bt_x.bg = bg
        self.bar.bts_base.bt_top.config(bg=bg)

    def titulo_color(self, bg='blue'):
        self.bar.lb_menu.config(bg=bg)

    def lee_toml(self):
        with open('mi_ventana/config.toml', "rb") as f:
            return tomllib.load(f)
        
    def asigna_icono(self, icono:str):
        self.bar.lb_menu.asigna_icono(icono)

    def tam(self, w:int=2):
        self.bar.tam(w)

    def mod_x(self, x):
        self.bar.mod_x(x)

    def mod_y(self, y):
        self.bar.mod_y(y)

    def item_cmd(self, nom, cmd):
        self.bar.item_cmd(nom, cmd)

    def asigna_icono(self, ico:str):
        ic = tk.PhotoImage(file=ico)
        self.iconphoto(True, ic)

    def asigna_icono_menu(self, ico:str):
        self.bar.asigna_icono_a_menu(ico)



if __name__=="__main__":
    app = MiVentana()
    app.bg('red')
    app.barra_color()
    app.titulo_color()
    app.mainloop()