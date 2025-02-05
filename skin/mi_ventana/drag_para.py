from tkinter import ttk
import tkinter as tk


class DragPara():
    def __init__(self, widget, parent=None, disable=None, releasecmd=None, *args, **kw):
        self.wg = widget
        self.disable = disable
        self.release_cmd = releasecmd
        self.parent = parent
        self._cnf_DragPara()

    def _cnf_DragPara(self):
        self.rz = self.wg.winfo_toplevel()
        # self.wg.bind('<Button-1>', self.posicion_relativa)
        # self.wg.bind('<ButtonRelease-1>', self.drag_unbind)
        # self.wg.bind('<ButtonPress-1>', self.posicion_relativa)
        # self.wg.bind('<ButtonRelease-1>', self.drag_unbind)

    def posicion_relativa(self, e):
        cx, cy = self.wg.winfo_pointerxy()
        geo = self.rz.geometry().split('+')
        self.ox, self.oy = int(geo[1]), int(geo[2])
        self.rel_x = cx - self.ox
        self.rel_y = cy - self.oy
        # self.wg.bind('<Motion>', self.drag_wid)
        self.wg.bind('<Motion>', self.drag_wid)
        # self.parent.title(f"x:{cx}, y:{cy} | {self.rel_x}, {self.rel_y}")

    def drag_wid(self, e):
        cx, cy = self.wg.winfo_pointerxy()
        x = cx - self.rel_x
        y = cy - self.rel_y
        if self.disable=='x':
            x = self.ox
        elif self.disable=='y':
            y = self.oy
        self.wg.geometry(f'+{x}+{y}')
        # self.parent.title(f"{x}, {y}")

    def drag_unbind(self, e):
        # self.wg.unbind('<Motion>')
        self.wg.unbind('<Motion>')
        if self.release_cmd != None:
            self.release_cmd()