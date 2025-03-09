from tkinter import ttk
import tkinter as tk


class KScroll(ttk.Scrollbar):
    def __init__(self, parent=None, **kw):
        super().__init__(master=parent, **kw)
        self.parent = parent
        self._configKScroll()

    def _configKScroll(self):
        self.st = ttk.Style()
        self.st.theme_use('default')
        bg = "black"
        fg = "gray20"
        self.st.configure(
            # "k.Vertical.TScrollbar",
            "Vertical.TScrollbar",
            gripcount=0,
            background=bg,
            darkcolor=bg,
            lightcolor=bg,
            troughcolor=fg,
            bordercolor=bg,
            relief='flat',
            arrowcolor=fg,
            borderwidth=0,
            thickness=2
        )
        self.st.map(
            # "k.Vertical.TScrollbar",
            "Vertical.TScrollbar",
            background=[('active',bg), ('!active',bg)],
            # arrowcolor=[("active",bg), ("!active",fg)]
        )
        # self.config(style="k.Vertical.TScrollbar")
        self.config(style="Vertical.TScrollbar")


class KTextoW(tk.Text):
    def __init__(self, parent, *args, **kw):
        super(KTexto, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self._configKTexto()

    def _configKTexto(self):
        self.bind('<Button-2>', self.toggleScroll)

    def dget(self, nom:str) -> str:
        self.dco = {
        }

    def setTema1(self):
        bg = "#0E0515"
        fg = "#D5D0BE"
        fo = "Consolas 9"
        self.config(
            bg=bg,
            fg=fg,
            font=fo,
            padx=2, pady=5,
            insertbackground=fg,
            selectbackground=fg,
            selectforeground=bg,
            relief='flat',
            border=0,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=bg,
            wrap='word',
            inactiveselectbackground=fg,
        )

    def msg(self, texto:str,tag:str='_tg', fg=None, bg=None, **kw):
        self.insert(tk.END, texto, (texto, tag))
        if fg: self.tag_config(tag, foreground=fg, **kw)
        if bg: self.tag_config(tag, background=bg, **kw)
        self.see(tk.END)

    def clear(self):
        self.delete(1.0, tk.END)

    def toClipboard(self, texto:str):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()

    def text(self):
        return self.get(1.0, tk.END).strip("\n")
    
    def setText(self, texto:str):
        self.delete(1.0, tk.END)
        self.insert(tk.END, texto)

    def msgNum(self, texto:str, num:int, tag:str=None, **kw):
        colores = [
            '#606A85', '#798560', '#748B91',
            '#30DFF3', '#748B91', '#B1B878',
            '#FFC335', '#E6E1CF', '#95E6CB'
        ]
        if not tag: f'_tg{num}'
        self.msg(texto, tag, fg=colores[num], **kw)

    def setScroll(self):
        self.scroll = KScroll(
            self, orient='vertical',
            command=self.yview
        )
        self.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(side='right', fill='y', pady=0, padx=0)

    def toggleScroll(self, e=None):
        if hasattr(self, 'scroll'):
            self.scroll.pack_forget()
            delattr(self, 'scroll')
        else:
            self.setScroll()


class KTexto(tk.Frame):
    def __init__(self, parent, *args, **kw):
        super(KTexto, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self._configKTexto()

    def _configKTexto(self):
        # self.parent.columnconfigure(0, weight=1)
        # self.parent.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.tex = tk.Text(master=self)
        self.tex.grid(row=0, column=0, sticky='wens')
        self.parent.bind('<Button-3>', self.toggleScroll)

    def setStyle(self, bg='#0E0515', fg='#D5D0BE', fo='Consolas 9'):
        self.tex.config(
            bg=bg,
            fg=fg,
            font=fo,
            padx=4, pady=5,
            insertbackground=fg,
            selectbackground=fg,
            selectforeground=bg,
            relief='flat',
            border=0,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=bg,
            wrap='word',
            inactiveselectbackground=fg,
        )

    def msg(self, texto:str,tag:str='_tg', fog=None, bog=None, **kw):
        """set text with tag"""
        self.tex.insert(tk.END, texto, (texto, tag))
        if fog: self.tex.tag_config(tag, foreground=fog, **kw)
        if bog: self.tex.tag_config(tag, background=bog, **kw)
        self.tex.see(tk.END)

    def clear(self):
        """clear all text"""
        self.tex.delete(1.0, tk.END)

    def toClipboard(self, texto:str):
        """copy text to clipboard"""
        self.tex.clipboard_clear()
        self.tex.clipboard_append(texto)
        self.tex.update()

    def text(self):
        """get text from widget"""
        return self.tex.get(1.0, tk.END).strip("\n")
    
    def setText(self, texto:str):
        """clear andset text to widget"""
        self.tex.delete(1.0, tk.END)
        self.tex.insert(tk.END, texto)

    def msgNum(self, texto:str, i:int=0, tag:str=None, **kw):
        """set text with tag and color predetermind"""
        colores = [
            '#606A85', '#798560', '#748B91',
            '#30DFF3', '#50C878', '#9AB200',
            '#FFC335', '#E6E1CF', '#95E6CB',
            '#494DCA', '#82586F', '#AF825D'
        ]
        if not tag: tag=f'_tg{i}'
        self.msg(texto, tag, fog=colores[i], **kw)

    def setScroll(self):
        """set scrollbar"""
        self.scroll = KScroll(
            self, orient='vertical',
            command=self.tex.yview
        )
        self.tex.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky='ns')
        
    def toggleScroll(self, e=None):
        """hide and show scrollbar"""
        if hasattr(self, 'scroll'):
            self.scroll.grid_forget()
            delattr(self, 'scroll')
        else:
            self.setScroll()

    def setKeywords(self, words:list, tag:str="key", **kw):
        """set keywords in text (resaltar palabras clave)"""
        self.tex.tag_config(tag, **kw)
        for word in words:
            ini = '1.0'
            while True:
                ini = self.tex.search(word, ini, stopindex=tk.END)
                if not ini: break
                fin = f'{ini}+{len(word)}c'
                self.tex.tag_add(tag, ini, fin)
                ini = fin
                print(word)

    def error(self, texto:str):
        """set error message predertermined"""
        d = dict(font='Consolas 9 bold')
        self.msg('!ER:', tag='errn', fog='black', bog='#FF1E4D', **d)
        self.msg(' ')
        self.msg(f"{texto}\n", tag='err_msg', fog='#FF1E4D', **d)


if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry('400x220')
    wg = KTexto(vn)
    wg.setScroll()
    wg.setStyle()
    wg.msg(texto="""Este es un ejemplo de texto donde algunas palabras serán resaltadas.
Las palabras clave en este texto serán destacadas automáticamente.
El texto puede contener múltiples palabras importantes."""*5)
    
    wg.setKeywords(
        ['palabras', 'texto', 'ejemplo'], foreground='#5E65E7', font="Consolas 10 bold"
    )
    wg.error('algo no va bien, no se eusand encontro algo con el directorio mencionado para la ejeucion del progra,a')
    wg.msgNum('segunda lineas mensaje cero\n', i=0)
    wg.msgNum('ffmpeg -copy video a:v copy codec av1 "salida.mp4')
    wg.setKeywords(
        ['lineas', 'clave', 'algunas', 'ffmpeg', '-copy', 'a:v'], tag='comm',
        foreground='#F04A27',
        font="Consolas 11"
    )
    wg.msgNum('nombre carpeta UNO1\n', i=1)
    wg.msgNum('nombre carpeta UNO2\n', i=2)
    wg.msgNum('█ nombre carpeta UNO3\n', i=3, font="Consolas 16")
    wg.msgNum('nombre carpeta UNO4\n', i=4)
    wg.msgNum('nombre carpeta UNO5\n', i=5)
    wg.msgNum('nombre carpeta UNO6\n', i=6)
    wg.msgNum('nombre carpeta UNO777\n', i=7)
    wg.msgNum(chr(9608)+' segunda lineas888\n', i=8)
    wg.msgNum('nombre carpeta UNO9\n', i=9)
    wg.msgNum('nombre carpeta UNO10\n', i=10)
    wg.msgNum('nombre carpeta UNO11\n', i=11)
    # wg.msgNum('ffmpeg -copy video a:v copy codec av1 "salida.mp4')
    # print("asdadasdad::: ", ord('█'))

    wg.grid(row=0, column=0, sticky='wens')
    vn.columnconfigure(0, weight=1)
    vn.rowconfigure(0, weight=1)
    vn.mainloop()