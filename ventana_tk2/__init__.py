import tkinter as tk
from tkinter import ttk
from ventana_tk2.barra import Barra
from tkinterdnd2 import TkinterDnD, DND_FILES
from ventana_tk2.widgets import MiGrip
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw, ImageTk
import threading
from io import BytesIO
import base64


class VentanaTk(TkinterDnD.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self._config_VentanaTk()
    
    def _config_VentanaTk(self):
        self.columnconfigure(0, weight=1)
        self.overrideredirect(True)

        self.bar = Barra(self)
        self.bar.grid(row=0, column=0, sticky='wens')
        self.setSize(800, 100)
        self.bar.cnf(mody=4) #colocar a 0 si hay margen top
        self.bar.ontop()

        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.getDrop)
        
        self.bar.fm_bts.bt_min.config(command=self.minimize)
        self.bar.fm_bts.bt_x.config(command=self.closeApp)
        self.setMenuItemTop("ventana 1", self.ventanaSizeUno)

    def _setIconTray(self, ico:str):
        # self.img_ = Image.open("tomi_cw2.png")
        self.img_ = Image.open(ico)
        self.icon = Icon(
            "uno", self.img_,
            menu=Menu(
                MenuItem("Restaurar ventana", self.showWindow),
                MenuItem("Cerrar", self.closeApp)
            )
        )
        threading.Thread(target=self.icon.run, daemon=True).start()

    def addGrip(self, bg="gray"):
        self.grip = MiGrip(self, bg=bg, w=6)
        self.grip.place(relx=0.996, rely=0.992, anchor="se")
        self.grip.bind("<Button-1>", self.grip.start_resize)  # Detectar clic inicial
        self.grip.bind("<B1-Motion>", self.grip.perform_resize)

    def setSize(self, w:int, h=int, tam=3/5):
        """size window and side (tam)"""
        self.geometry(f"{w}x{h}")
        self.bar.setSize(w, h, tam=tam)
        self.W, self.H = w, h

    def toClipboard(self, texto:str):
        """texto to clipboard"""
        self.clipboard_clear()
        self.clipboard_append()
        self.update()

    def getDrop(self, e):
        return self.fix(e.data)

    def fix(self, texto:str) -> list:
        """retorna list de strings sin llaves"""
        def getIndices(texto:str):
            indices = []
            i = 0
            for _ in range(texto.count(":")):
                if ":" in texto[i:]:
                    i = texto.index(":", i+1)
                    indices.append(i-1)
            indices.append(-1)
            return indices
        rutas = []
        inicio = 0
        for fin in getIndices(texto)[1:]:
            ruta = texto[inicio:] if fin==-1 else texto[inicio:fin]
            rutas.append(ruta.strip("{} "))
            inicio = fin
        return rutas
    
    def minimize(self):
        self.withdraw()

    def showWindow(self):
        self.deiconify()

    def closeApp(self):
        if hasattr(self, 'icon'):
            self.icon.stop()
        self.bar.cerrar()

    def ventanaSizeUno(self):
        self.geometry(f"{self.W}x{self.H}")

    def setMenuItemTop(self, texto:str, cmd):
        self.bar.menuItem(texto, cmd)

    def setBg(self, color:str):
        self.config(bg=color)
        self.grip.config(bg=color)

    def setIconAll(self, ico:str):
        self.iconAll = tk.PhotoImage(file=ico)
        self.bar.setIconMenu(image=self.iconAll)
        self._setIconTray(ico)

    def setIconData(self, b64:str):        
        ico_data = base64.b64decode(b64)
        self.img_ = Image.open(BytesIO(ico_data))
        self.icotk = ImageTk.PhotoImage(self.img_.resize((14, 14)))
        self.bar.setIconMenu(image=self.icotk)

        self.icon = Icon(
            "uno", self.img_,
            menu=Menu(
                MenuItem("Restaurar ventana", self.showWindow),
                MenuItem("Cerrar", self.closeApp)
            )
        )
        threading.Thread(target=self.icon.run, daemon=True).start()



    
