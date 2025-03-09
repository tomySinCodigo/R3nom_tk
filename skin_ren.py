import tkinter as tk
from tkinter import ttk
from skin.kbasewg import KButton, KEntry, KNotebook
from skin.kcombobox import KCombobox
from skin.ktreeview import KTreeview
from skin.ktexto import KTexto


class SkinRen(tk.Frame):
    def __init__(self, parent, *args, **kw):
        super(SkinRen, self).__init__(master=parent, *args, **kw)
        self._configSkinRen()

    def _configSkinRen(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        fmtop = tk.Frame(self, bg='red')
        fmtop.grid(row=0, column=0, sticky='wens')
        fmtop.columnconfigure(1, weight=1)
        fmtop.rowconfigure(0, weight=1)
        self.bt_rename = KButton(fmtop, text='RENAME')
        self.bt_rename.setStyle()
        self.bt_rename.grid(row=0, column=0, sticky='wens')

        fondo = '#252722'
        bg_fm = '#35332E'
        fmtopd = tk.Frame(fmtop, bg='blue')
        fmtopd.grid(row=0, column=1, sticky='wens')
        fmtopd.columnconfigure(0, weight=1)
        fmtopd.rowconfigure((0,1,2), weight=1, minsize=22)
        fm1 = tk.Frame(fmtopd, bg=bg_fm, height=23)
        fm1.grid(row=0, column=0, sticky='wens')
        fm1.columnconfigure(2, weight=1)
        fm1.rowconfigure(0, weight=1)
        fm2 = tk.Frame(fmtopd, bg=bg_fm, height=23)
        fm2.grid(row=1, column=0, sticky='wens')
        fm2.columnconfigure(0, weight=1)
        fm2.rowconfigure(0, weight=1)
        fm_vista = tk.Frame(fmtopd, bg=bg_fm)
        fm_vista.grid(row=2, column=0, sticky='wens')
        fm_vista.columnconfigure(0, weight=1)
        fm_vista.rowconfigure(0, weight=1)

        self.cmb_cores = KCombobox(fm1, width=11)
        self.cmb_cores.setStyle(fo=("Consolas",12, "bold"))
        self.cmb_cores.grid(row=0, column=0, sticky='we')
        self.bt_coresinfo = KButton(fm1, width=3, text="i", padding=0)
        self.bt_coresinfo.setStyle(
            fo=("Consolas",10, "bold"),
            bg='#1E1C1A', fg='#FFCE6F',
            nom_s='k2',
        )
        self.bt_coresinfo.grid(row=0, column=1, sticky='we', padx=1, pady=0, ipady=0)

        self.en_plantilla = KEntry(fm1)
        self.en_plantilla.setStyle()
        self.en_plantilla.grid(row=0, column=2, sticky='wens', pady=1, padx=2)

        self.en_tags = KEntry(fm2)
        self.en_tags.setStyle()
        self.en_tags.grid(row=0, column=0, sticky='wens', pady=1, padx=2)
        self.bt_cleartags = KButton(fm2, text='X', width=3, padding=0)
        self.bt_cleartags.setStyle(
            fo=("Consolas",10, "bold"),
            bg='#1E1C1A', fg='#FFCE6F',
            nom_s='k2',
        )
        self.bt_cleartags.grid(row=0, column=1, sticky='we', ipady=0, padx=2)
        self.cmb_tags = KCombobox(fm2,height=20, width=15)
        # self.cmb_tags.setStyle()
        self.cmb_tags.setStyle(
            fg='#B3B3B3', bg='#120D0D', fo=("Consolas",12, "bold"),
            fgm='#B3B3B3'
        )
        self.cmb_tags.grid(row=0, column=2, sticky='we')

        self.en_newname = KEntry(fm_vista)
        self.en_newname.grid(row=0, column=0, sticky='wens',pady=1,padx=2)
        self.bt_recarga = KButton(fm_vista, text='R', width=3)
        self.bt_recarga.setStyle()
        self.bt_recarga.grid(row=0, column=1, sticky='wens', padx=4)
        self.bt_previa = KButton(fm_vista, text='PREVIEW')
        self.bt_previa.setStyle(bg='#35332E', fg='#FFCE6F', fo="Consolas 8")
        self.bt_previa.grid(row=0, column=2, sticky='wens')
        # self.en_newname.setStyle(bg='gray25')
        # self.en_newname.setStyle(bg=fondo)
        fondo_en = "#3B3933"
        self.en_newname.setStyle(bg=fondo_en)


        bg = bg_fm
        self.pw = tk.PanedWindow(
            self, orient=tk.VERTICAL, relief='flat',
            background=bg,
            proxybackground=bg,
            proxyrelief='flat',
            sashrelief='flat',
            border=0
        )
        self.pw.grid(row=1, column=0, sticky='wens')
        self.pw.columnconfigure(0, weight=1)
        self.pw.rowconfigure(1, weight=1)

        self.tree = KTreeview(self.pw, bg=fondo)
        self.tree.setStyle()
        self.pw.add(self.tree)
        self.tex = KTexto(self.pw)
        self.tex.setStyle(bg=fondo)
        self.tex.setScroll()
        self.pw.add(self.tex)
        self.pw.sash_place(0,0,60)


if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry('600x320')
    wg = SkinRen(vn)

    wg.cmb_tags.items = list(range(10))


    wg.grid(row=0, column=0, sticky='wens')
    vn.columnconfigure(0, weight=1)
    vn.rowconfigure(0, weight=1)
    vn.mainloop()

