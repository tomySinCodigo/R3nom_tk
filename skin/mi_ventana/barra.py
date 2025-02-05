from ctypes import windll
import tkinter as tk
from skin.mi_ventana.frame_botones import FrameBotones
from skin.mi_ventana.label_menu import LabelMenu
from skin.mi_ventana.posicion_ventana import PosicionVentana
from skin.mi_ventana.drag_para import DragPara
from skin.mi_ventana.frame_drag import FrameDrag
from tkinter import Button
# from mi_ventana.mi_texto import MiTexto


def set_appwindow(root):
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    hwnd = windll.user32.GetParent(root.winfo_id())
    style = windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
    # re-assert the new window style
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())

class Barra(tk.Frame):
    def __init__(self, parent, bg='#303030', height=6, *args, **kw):
        super(Barra, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self.bg = bg
        self.alto = height
        self._widget_Barra()
        self.estado_max = False
        self.POS_IZ = True
        self.MODX = 0
        self.MODY = 0
        self.TOP = True
        self.ico_on = None

    def _widget_Barra(self):
        self.config(bg=self.bg, height=self.alto)
        self.lb_menu = LabelMenu(self)
        self.lb_menu.grid(row=0, column=0)

        # TITULO
        self.text_titulo = tk.Text(
            self, height=1, padx=6, font=("Consolas", 8, "bold"),
            bg='#303030', fg="#E5E5E5", relief="flat",
            selectbackground='#202020',
            selectforeground='orange',
        )
        self.text_titulo.grid(row=0, column=1, sticky='we')
        # self.text_titulo.insert("end", "TITULO SECUNDARIO FILE: c:/folder/mi_directorio")
        self.text_titulo.config(state='disabled')

        # agregando botones basicos
        self.bts_base = FrameBotones(self, bgh='black')
        self.bts_base.grid(row=0, column=3, sticky='we')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        # comandos
        self.bts_base.bt_x.config(command=self.cerrar)
        # self.parent.bind('<Button-2>', self.cerrar)
        self.parent.bind('<less>', self.cerrar)

        # CENTRAR VENTANA
        self.pv = PosicionVentana(self.parent, 600, 16)
        self.pv.centrar()

        # asignando metodos
        self.bts_base.bt_min.config(command=self.minimiza)
        self.bts_base.bt_fw.config(command=self.maximiza)
        self.bts_base.bt_izq.config(command=self.izq)
        self.bts_base.bt_top.config(command=self.ontop)

        # var menu
        self.menu = self.lb_menu.menu
        self.RUTA_ICO = self.bts_base.get_ruta()

    def cerrar(self, e=None):
        self.parent.destroy()

    def minimiza(self, e=None):
        self.parent.overrideredirect(0)
        self.parent.wm_iconify()
        self.parent.bind('<FocusIn>', self.iconifica)

    def iconifica(self, e=None):
        a = self.parent.wm_overrideredirect()
        if a is None:
            self.parent.overrideredirect(1)
            # set_appwindow(root=self)
            set_appwindow(root=self.parent)

    def maximiza(self, e=None):
        if self.estado_max:
            self.parent.wm_state('normal')
            self.estado_max = False
            # self.btn_vf.config(image=self.ico_vf)
        else:
            self.parent.wm_state('zoomed')
            self.estado_max = True
            # self.btn_vf.config(image=self.ico_vc)

    def izq(self):
        # self.pv.d['mody'] = 4
        # self.pv.d['modx'] = 4
        if self.POS_IZ:
            self.pv.izq()
            self.POS_IZ = False
        else:
            self.pv.der()
            self.POS_IZ = True

    def mod_y(self, y=0):
        self.pv.d['mody'] = y

    def mod_x(self, x=0):
        self.pv.d['modx'] = x

    def tam(self, w=3):
        self.pv.d['tam'] = w

    def item_cmd(self, nom, cmd):
        self.menu.add_command(label=nom, command=cmd)

    def msg(self, texto, tag='_tg', fg=None, bg=None, **kwargs):
        self.text_titulo.config(state='normal')
        self.text_titulo.insert('end', texto, (texto, tag))
        if fg:
            self.text_titulo.tag_config(tag, foreground=fg, **kwargs)
        if bg:
            self.text_titulo.tag_config(tag, background=bg, **kwargs)
        self.text_titulo.config(state='disabled')

    def asigna_icono_a_menu(self, icono):
        self.lb_menu.asigna_icono(icono)

    def _top(self, b=True):
        self.parent.attributes('-topmost', b)

    def icono_a_btn(self, btn:Button, ico:str):
        self.ico_on = tk.PhotoImage(file=f"{self.RUTA_ICO}/{ico}")
        btn.config(image=self.ico_on)

    def ontop(self):
        if self.TOP:
            self._top()
            self.TOP = False
            self.icono_a_btn(self.bts_base.bt_top, 'unlock.png')
        else:
            self._top(False)
            self.TOP = True
            self.icono_a_btn(self.bts_base.bt_top, 'lock.png')




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

    def titulo_color(self, bg='blue'):
        self.bar.lb_menu.config(bg=bg)


if __name__=="__main__":
    app = MiVentana()
    app.bg('red')
    app.barra_color()
    app.titulo_color()
    app.mainloop()