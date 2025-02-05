from tkinter import ttk
import tkinter as tk


class FrameDrag(tk.Frame):
    def __init__(self, parent=None, disable=None, releasecmd=None, *args, **kw):
        super(FrameDrag, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self.disable = disable
        self.release_cmd = releasecmd
        self._widget_FrameDrag()
        
    def _widget_FrameDrag(self):
        if type(self.disable)=='str':
            self.disable = self.disable.lower()
        self.rz = self.parent.winfo_toplevel()
        self.bind('<Button-2>', self.cerrar)
        # self.parent.bind('<Button-1>', self.posicion_relativa)
        # self.parent.bind('<ButtonRelease-1>', self.drag_unbind)

        # self.grip_e.config(text='\n\n')
        # AGEGANDO LOS GRIPS
        self.grip_se = self.mkGrip(1.0, 1.0, 'se')
        # self.grip_e = self.mkGrip(1.0, 0.5, 'e')
        # self.grip_ne = self.mkGrip(1.0, 0, 'ne')
        # self.grip_n = self.mkGrip(0.5, 0, 'n')
        # self.grip_nw = self.mkGrip(0, 0, 'nw')
        # self.grip_w = self.mkGrip(0, 0.5, 'w')
        self.grip_sw = self.mkGrip(0, 1.0, 'sw')
        # self.grip_s = self.mkGrip(0.5, 1.0, 's')

    def cerrar(self, e=None):
        self.parent.destroy()
    
    def posicion_relativa(self, e):
        cx, cy = self.parent.winfo_pointerxy()
        geo = self.rz.geometry().split('+')
        self.ox, self.oy = int(geo[1]), int(geo[2])
        self.rel_x = cx - self.ox
        self.rel_y = cy - self.oy
        self.bind('<Motion>', self.drag_wid)
        # self.parent.title(f"x:{cx}, y:{cy} | {self.rel_x}, {self.rel_y}")

    def drag_wid(self, e):
        cx, cy = self.parent.winfo_pointerxy()
        x = cx - self.rel_x
        y = cy - self.rel_y
        if self.disable=='x':
            x = self.ox
        elif self.disable=='y':
            y = self.oy
        self.rz.geometry(f'+{x}+{y}')
        # self.parent.title(f"{x}, {y}")

    def drag_unbind(self, e):
        self.unbind('<Motion>')
        if self.release_cmd != None:
            self.release_cmd()

    def mkGrip(self, x, y, anchor:str, bg='gray10'):
        # grip = tk.Label(self.parent, bg=bg)
        grip = tk.Label(self.parent, bg=bg)
        grip.place(relx=x, rely=y, anchor=anchor)
        grip.bind('<B1-Motion>',lambda e,mode=anchor:self._enMovimiento(e,mode))
        return grip
    
    def agrega_boton_cerrar(self):
        self.btn_x = tk.Button(
            self.parent, text='x', bg='red', fg='white', command=self.cerrar,
            height=1, relief='flat',
            pady=-1,
        )
        # s = ttk.Style()
        # s.theme_use('clam')
        # self.btn_x = ttk.Button(
        #     self.parent, text='x', command=self.cerrar, width=1,
        #     takefocus=False,
        #     padding=0,
        # )
        self.btn_x.place(relx=1.0, rely=0, anchor='ne')

    def _enMovimiento(self, e, modo=None):
        # x, y = self.winfo_rootx(), self.winfo_rooty()
        # abs_x = self.winfo_pointerx()-x
        # abs_y = self.winfo_pointery()-y
        # w, h = self.winfo_width(), self.rz.winfo_height()
        x, y = self.parent.winfo_rootx(), self.parent.winfo_rooty()
        abs_x = self.parent.winfo_pointerx()-x
        abs_y = self.parent.winfo_pointery()-y
        w, h = self.parent.winfo_width(), self.parent.winfo_height()
        hmin = 40

        if modo=='se' and abs_x>0 and abs_y>0:
            self._gm_wh(abs_x, abs_y)
        elif modo=='e':
            if h>0 and abs_x>0:
                self._gm_wh(abs_x, h)
        elif modo=='ne' and abs_x>0:
            y+=abs_y
            h-=abs_y
            if h>hmin:
                self._gm(abs_x, h, y, x)
        elif modo=='n':
            h-=abs_y
            y+=abs_y
            if h>0 and w>0:
                self._gm(w, h, x, y)
        elif modo=='nw':
            w-=abs_x
            h-=abs_y
            x+=abs_x
            y+=abs_y
            if h>hmin and w>0:
                self._gm(w,h,x,y)
        elif modo=='w':
            w-=abs_x
            x+=abs_x
            if h>0 and w>0:
                self._gm(w,h,x,y)
        elif modo=='sw':
            w-=abs_x
            h-=(h-abs_y)
            x+=abs_x
            if h>hmin and w>0:
                self._gm(w,h,x,y)
        elif modo=='s':
            h-=(h-abs_y)
            if h>0 and w>0:
                self._gm(w,h,x,y)

    def _gm_wh(self, w, h):
        self.parent.geometry(f'{w}x{h}')

    def _gm(self, w, h, x, y):
        self.parent.geometry(f'{w}x{h}+{x}+{y}')


class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("600x300")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        wg = FrameDrag(self)
        wg.grid(row=0, column=0, sticky="wens")
        self.overrideredirect(True)
        wg.agrega_boton_cerrar()
        

if __name__=="__main__":
    app = Ventana()
    app.mainloop()