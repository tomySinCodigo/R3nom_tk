import tkinter as tk
from tkinter import ttk



class KButton(ttk.Button):
    def __init__(self, parent, *args, **kw):
        super(KButton, self).__init__(master=parent, *args, **kw)
        self._configKButton()

    def _configKButton(self):
        ...

    def setStyle(
        self, s:str=None, fg='gray70', bg='#1E2424',
        fgp='white', bgp='black',
        fo=("Consolas", 9, 'normal'),
        fga='gray80', bga='#1E2732',
        nom_s = 'k'
    ):
        if not s:
            s=ttk.Style()
            s.theme_use('default')
        """fg, bg, [fgp, bgp]pressed, [fga, bga]active"""
        s.configure(
            f"{nom_s}.TButton",
            background=bg, foreground=fg,
            relief='flat', highlightthickness=0,
            borderwidth=0, font=fo,
            highlightcolor='red'
        )
        s.map(
            f"{nom_s}.TButton",
            background=[
                ('pressed', bgp), ('active',bga),
            ],
            foreground=[
                ('pressed', fgp), ('active',fga),
                ('disabled', '#59564D'), ('!disabled', fg)
            ],
            #relief=[('pressed', 'raised'), ('!pressed', 'flat')]
            #relief=[('active', 'sunken'), ('!active', 'flat')]
        )
        self.config(style=f"{nom_s}.TButton")

    def disabled(self):
        self.config(state=tk.DISABLED)

    def enable(self):
        self.config(state=tk.NORMAL)



class KEntry(ttk.Entry):
    def __init__(self, parent, *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self._configKEntry()

    def _configKEntry(self):
        self.TEXTO = tk.StringVar()
        self.config(textvariable=self.TEXTO)

    def text(self) -> str:
        return self.TEXTO.get() # self.get() same

    def setText(self, texto:str):
        self.TEXTO.set(texto)

    def setStyle(
        self, s:str=None, bg='gray10', fg='ivory3',
        bga='#10061E', fga='white'
    ):
        if not s:
            s=ttk.Style()
            s.theme_use('default')
        # fg=self.cget('foreground')
        s.configure(
            'k.TEntry',
            fieldbackground=bg,
            foreground=fg,
            insertcolor=fg,
            insertwidth=2,
            bordercolor=bg,
            # bordercolor='red',
            borderwidth=0,
            relief='ridge',
            selectborderwidth=0,
            selectforeground=bg,
            selectbackground=fg
        )
        s.map(
            "k.TEntry",
            fieldbackground=[('focus', bga), ('!focus', bg)],
            foreground=[('focus', fga), ('!focus', fg)]
        )
        self.config(style='k.TEntry')
        self.update()

    def cmdEnter(self, metodo):
        self.bind('<Return>', metodo)

    def cmdKeyPressed(self, metodo):
        self.bind('<Key>', metodo)

    def clear(self):
        self.setText('')


class KNotebook(ttk.Notebook):
    def __init__(self, parent, *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self._configKNotebook()

    def _configKNotebook(self):
        self.BG = '#1E1E1E'
        self.pag1 = tk.Frame(self, bg=self.BG)
        self.pag2 = tk.Frame(self, bg=self.BG)
        # txt = "iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA8ElE" \
        # "QVR4nK1SOY7CQBCEhYAVz4APEHJ8BR6wT1gCf4QjnwAzXcVIjiZZbc4n+IZRYQ5jYUtIjNRyq7vKXX20Wp98pP0"\
        # "A+JPJbwTHGLvOue+CiP8Q9iOZfMWUE+ZFFWwAO5EWSdvd4gD2il1z6yeSmc1IHLMs64cQBkmSfB0OfiqT770fKi"\
        # "cMyUm5p6X+7JzrCEiaV1USqeJ5nreVkw/g904UGMCWtLmqlKWSSFUFwELtCNtARPrcYw2xLFWyCjDS27dW6rXKZ"\
        # "TgaRNEnJ7LqcMxsXF36+rGOqtRiHQBWLw8gxtirOwDlJLfxit46uXffGQMyDIuq6kwEAAAAAElFTkSuQmCC"
        # self.icop1 = tk.PhotoImage(data=txt)
        # d = dict(
        #     image=self.icop1,
        #     compound=tk.LEFT
        # )
        # self.add(self.pag1, text='CONFIGS', **d)
        self.add(self.pag1, text='CONFIGS')
        self.add(self.pag2, text='PESTAÑA DOS')
        self.PAGES = [self.pag1, self.pag2]
        self.IX_PAG = 0

    @property
    def currentPage(self) -> str:
        return self.select()

    @currentPage.setter
    def currentPage(self, i:int=0):
        self.select(i)
        self.IX_PAG = i

    def currentIndex(self) -> int:
        return self.index(self.select())

    def togglePages(self):
        self.IX_PAG = self.currentIndex()
        self.IX_PAG += 1
        self.IX_PAG = self.IX_PAG if self.IX_PAG<len(self.PAGES) else 0
        self.currentPage = self.IX_PAG

    def setStyle(self, s:str=None, bg_bar="#282828", fg='#CAC8AC'):
        bg = bg_bar
        if not s:
            s=ttk.Style()
            s.theme_use('default')
        s.theme_create(
            'k', parent='default',
            settings={
                '.':{
                    'configure':dict(
                        background=bg_bar,
                        foreground='gray40',
                        # tabposition='wn',
                        tabposition='ne',
                        relief='flat',
                        tabborders=0,
                        raiseselect=False,
                        font="Consolas 8 bold"
                    )
                },
                # 'TLabel':{
                #     'configure':dict(foreground="red")
                # },
                'TNotebook':{
                    'configure':dict(
                        tabmargins=[0,5,2,0],
                        borderwidth=0,
                    )
                },
                'TNotebook.Tab':{
                    'configure':dict(
                        relief='flat',
                        takefocus=False,
                        bordercolor=bg,
                        darkcolor=bg,
                        lightcolor=bg,
                        padding=[6,0],
                        background=bg,
                        borderwidth=0
                    ),
                    'map':dict(
                        background=[('selected', self.BG)],
                        foreground=[('selected', fg)],
                        expand=[('selected', [1, 1, 1, 0])]
                    )
                }
            }
        )
        # s.layout('k.TNotebook.Tab', []) #activar para que no haya tabs
        # self.config(style='k.TNotebook')
        s.theme_use('k')


if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry('400x100')
    # wg = KButton(vn, text="RENOM", compound=tk.TOP)
    # wg.setStyle(fo="Consolas 8 bold")
    # ico = tk.PhotoImage(file='coreren_32b24.png')
    # wg.config(image=ico)

    # wg = KEntry(vn, font="Consolas 10 bold", state='normal')
    # # wg.setStyle(fg='gray70')
    # wg.setStyle()
    # wg.setText("hola como estas perro")
    # def enter(e):
    #     print(wg.text())
    #     # print(wg.get())
    # def key(e):
    #     letra = e.char
    #     res = f"vocal: {letra}" if letra in 'aeiou' else letra
    #     print(res)
    # wg.cmdEnter(enter)
    # wg.cmdKeyPressed(key)


    # NOTEBOOK
    wg = KNotebook(vn)
    wg.setStyle()


    bt = tk.Button(vn, text='toggle', command=wg.togglePages)
    bt.place(relx=0.92, rely=0.90, anchor='center')
    # NOTEBOOK


    wg.grid(row=0, column=0, sticky='wens', ipady=0)
    vn.columnconfigure(0, weight=1)
    vn.rowconfigure(0, weight=1)
    vn.mainloop()