from tkinter import ttk
import tkinter as tk
from skin.wtk.ktreeview import KTreeview
from skin.wtk.kombobox import Kombobox
from skin.wtk.ktreeview import KTreeview
from skin.wtk.ktexto import KText


class OSkin(tk.Frame):
    def __init__(self, parent, *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self._config_OSkin()
        
    def _config_OSkin(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.fm_barra = tk.Frame(self, bg='orange')
        self.fm_barra.grid(row=0, column=0, sticky="wens")
        self.fm_barra.columnconfigure(1, weight=1)
        self.fm_barratop = tk.Frame(self.fm_barra, bg='skyblue')
        self.fm_barratop.grid(row=0, column=1, sticky="wens")
        self.fm_barratop.columnconfigure(1, weight=1)
        self.fm_barrabot = tk.Frame(self.fm_barra, bg='green')
        self.fm_barrabot.grid(row=1, column=1, sticky="wens")
        self.fm_barrabot.columnconfigure(0, weight=1)
        
        bg = '#303430'
        bga = 'black'
        fg = 'azure'
        fga = 'white'
        
        self.sbt = {
            'relief':'flat',
            #'background':bg,
            'background':'#202020',
            'foreground':fg,
            'activebackground':bga,
            'activeforeground':fga,
            'font':('Consolas', 8, 'bold')
        }
        self.sen = {
            'relief':'flat',
            'background':bg,
            'foreground':fg,
            'highlightbackground':bg,
            'highlightthickness':0,
            'insertbackground':fg
        }
        
        self.ss = ttk.Style()
        self.ss.theme_use('alt')
        
        self.bt_renamer = tk.Button(self.fm_barra, text="RENAMER", **self.sbt)
        self.bt_renamer.grid(row=0, column=0, sticky="wens", rowspan=2)
        #self.cmb_core = ttk.Combobox(self.fm_barratop, width=10)
        self.cmb_core = Kombobox(self.fm_barratop, width=10)
        self.cmb_core.grid(row=0, column=0, sticky="wens")
        self.cmb_core.estilo(self.ss)
        self.PLANTILLA = tk.StringVar()
        self.en_plantilla = tk.Entry(self.fm_barratop, textvariable=self.PLANTILLA, **self.sen)
        self.en_plantilla.grid(row=0, column=1, sticky="wens")
        self.bt_previa = tk.Button(self.fm_barratop, text='PREVIA', **self.sbt)
        self.bt_previa.grid(row=0, column=2, sticky="wens")
        
        self.NOMBRE = tk.StringVar()
        self.en_nombres = tk.Entry(self.fm_barrabot, textvariable=self.NOMBRE, **self.sen)
        self.en_nombres.grid(row=0, column=0, sticky="wens")
        self.bt_recarga = tk.Button(self.fm_barrabot, text='R', width=3, **self.sbt)
        self.bt_recarga.grid(row=0, column=1, sticky="wens")
        self.cmb_nombres = Kombobox(self.fm_barrabot, width=14, values=['uno','persona','nombrelargo'])
        self.cmb_nombres.grid(row=0, column=2, sticky="wens")
        self.cmb_nombres.estilo(self.ss, fg='#FFC353', fgm='#FFC353')
        self.cmb_nombres.config(width=14)
        
        bgt = '#151500'
        self.pw = tk.PanedWindow(
            self, orient=tk.VERTICAL, relief='flat',
            background=bgt,
            proxybackground=bg,
            proxyrelief='flat',
            sashrelief='flat'
        )
        self.pw.grid(row=1, column=0, sticky="wens")
        self.tree = KTreeview(self, height=3)
        self.tree.estilo(self.ss, bg=bgt)
        # self.tex = MiTexto(self.pw)
        # self.tex.config(bg=bgt)
        self.tex = KText(self.pw, ss=self.ss)
        self.tex.cnf(bg=bgt)
        self.pw.add(self.tree)
        self.pw.add(self.tex)
        self.rowconfigure(1, weight=1)

    def msg(self, texto, **kw):
        """texto, tag, fg, bg"""
        self.tex.msg(texto=texto, **kw)

    def msgNum(self, texto, i=0, **kw):
        """texto, i[0-8], kw[tag, fg, bg]"""
        self.tex.msgNum(texto, i, **kw)
        
        

if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('550x250')
    wg = OSkin(rz)
    wg.grid(row=0, column=0, sticky='wens')
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('OSkin')
    rz.mainloop()