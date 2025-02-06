from tkinter import ttk
import tkinter as tk
from tkinter.ttk import Style


class Colores:
    def __init__(self):
        # self.bg = '#191C21'
        self.bg = '#151500'
        self.fg = 'white'
        self.select_bg = 'black'
        self.select_fg = 'skyblue'
        self.scroll_bg = '#150C1B'
        self.scroll_fg = 'gray20'
        self.fo = ('Lucida Consoles', 8, 'normal')
        self.relief = 'flat'
        self.bd = 0

class KScroll(ttk.Scrollbar):
    def __init__(self, parent, ss:Style, *args, **kw):
        super(KScroll, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self.ss = ss
        self._configKScroll()

    def _configKScroll(self):
        color = Colores()
        self.ss.configure(
            # "s1.Vertical.TScrollbar",
            "Vertical.TScrollbar",
            gripcount=0,
            background=color.scroll_fg,
            darkcolor=color.scroll_bg,
            lightcolor=color.scroll_bg,
            troughcolor=color.scroll_fg,
            bordercolor=color.scroll_bg,
            relief='flat'
        )
        self.ss.map(
            # "s1.Vertical.TScrollbar",
            "Vertical.TScrollbar",
            background=[("!active", color.scroll_bg), ("active", color.scroll_bg)],
            arrowcolor=[("active", color.scroll_bg), ("!active", color.scroll_fg)]
        )
        self.config(style="Vertical.TScrollbar")


class KText(tk.Frame):
    def __init__(self, parent=None, ss=None, *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self.ss = ss
        self._config_KText()

    def _config_KText(self):
        color = Colores()
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.tex = tk.Text(
            self,
            bg=color.bg,
            fg=color.fg,
            padx=8, pady=5,
            insertbackground=color.fg,
            selectbackground=color.select_bg,
            selectforeground=color.select_fg,
            font=color.fo,
            relief=color.relief,
            border=color.bd
        )
        self.tex.grid(row=0, column=0, sticky='wens')
        # self.ss = ttk.Style()
        # self.ss.theme_use('alt')
        if self.ss:
            self.setScroll(self.ss)

    def cnf(self, **kw):
        self.tex.config(**kw)

    def msg(self, texto:str, tag:str='_tag', fg=None, bg=None, **kw):
        self.tex.insert('end', texto, (texto, tag))
        if fg:
            self.tex.tag_config(tag, foreground=fg, **kw)
        if bg:
            self.tex.tag_config(tag, background=bg, **kw)

    def clear(self):
        self.tex.delete('0.1', 'end')

    def toClipboard(self, texto:str):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()

    def insert(self, texto:str):
        self.tex.insert('end', texto)
        self.tex.see('end')

    def text(self):
        return self.tex.get('0.1', 'end').strip('\n')
    
    def see(self):
        self.tex.see('end')

    def msgNum(self, texto, i=6, **kw):
        colores = [
            '#606A85', '#798560', '#748B91',
            '#30DFF3', '#748B91', '#B1B878',
            '#FFC335', '#E6E1CF', '#95E6CB'
            ]
        self.msg(f'{texto}', f'tg_{i}', colores[i], **kw)

    def setScroll(self, ss:Style):
        self.scroll = KScroll(
            self, ss, orient='vertical',
            command=self.tex.yview
        )
        self.scroll.grid(row=0, column=1, sticky='ns')
        self.tex.config(yscrollcommand=self.scroll.set)

    def error(self, texto:str):
        d = {'font':'Consolas 9 bold'}
        self.msg('!ER:', tag='errn', fg='black', bg='#FF1E4D', **d)
        self.msg(' ')
        self.msg(f"{texto}\n", tag='err_msg', fg='#FF1E4D', **d)




if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry("550x320")

    wg = KText(vn)
    wg.grid(row=0, column=0, sticky='wens')
    wg.columnconfigure(0, weight=1)
    wg.rowconfigure(0, weight=1)

    wg.error('algo no va bien, no se eusand encontro algo con el directorio mencionado para la ejeucion del progra,a')
    wg.msgNum('segunda lineas\n', i=0)
    wg.msgNum('nombre carpeta UNO1\n', i=1)
    wg.msgNum('nombre carpeta UNO2\n', i=2)
    wg.msgNum('nombre carpeta UNO3\n', i=3)
    wg.msgNum('nombre carpeta UNO4\n', i=4)
    wg.msgNum('nombre carpeta UNO5\n', i=5)
    wg.msgNum('nombre carpeta UNO6\n', i=6)
    wg.msgNum('nombre carpeta UNO777\n', i=7)
    wg.msgNum('segunda lineas888\n', i=8)


    texto = """What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.

Where can I get some?
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
"""
    wg.msg(texto)
    
    # s = ttk.Style()
    # s.theme_use('alt')

    vn.mainloop()