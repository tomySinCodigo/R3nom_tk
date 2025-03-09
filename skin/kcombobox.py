from tkinter import ttk
import tkinter as tk
from typing import Iterable


class KCombobox(ttk.Combobox):
    def __init__(self, parent,*args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self._config_KCombobox()

    def _config_KCombobox(self):
        self.ELEMENTOS = []

    @property
    def items(self) -> Iterable:
        """get items"""
        return self.ELEMENTOS

    @items.setter
    def items(self, lista:Iterable):
        """set items"""
        self.ELEMENTOS = lista
        self.config(state='normal')
        self.config(values=self.ELEMENTOS, state='readonly')

    @property
    def currentItem(self) ->str:
        return self.get()

    @currentItem.setter
    def currentItem(self, elem:str):
        self.set(elem)

    @property
    def currentIndex(self) -> int:
        return self.current()

    @currentIndex.setter
    def currentIndex(self, i:int):
        self.current(i)

    def item(self, elem:str):
        valores = list(self['values'])
        valores.append(str(elem))
        self['values'] = valores

    def cmdSelected(self, metodo):
        self.bind('<<ComboboxSelected>>', metodo)

    def setStyle(
        self, fg='RoyalBlue1', bg='black',
        fgm='RoyalBlue1', bgm='black',
        fo=('Consolas',12,'normal')
    ):
        s = ttk.Style()
        s.theme_use('default')
        s.configure(
            'k.TCombobox',
            foreground=fg,
            background=bg,
            bordercolor=bg,
            borderwidth=0,
            arrowcolor=fg,
            relief='flat',
            selectbackground=bg,
            selectforeground=fg,
            takefocus=False,
            font=fo,
            padding=0
        )
        s.map(
            'k.TCombobox',
            fieldbackground=[('readonly',bg), ('!readonly',bg)],
            background=[('readonly', bg)],  # Fondo del área de la flecha
            arrowcolor=[('readonly', fg)],  # Color de la flecha
            foreground=[('readonly', fg)],  # Color del texto
            selectbackground=[('readonly', bg)],  # Fondo del elemento seleccionado
            selectforeground=[('readonly', fg)]  # Color del texto del elemento seleccionado

        )
        
        self.option_add('*TCombobox*Listbox.background', bgm)
        self.option_add('*TCombobox*Listbox.foreground', fgm)
        self.option_add('*TCombobox*Listbox.selectBackground', fg)
        self.option_add('*TCombobox*Listbox.selectForeground', bg)
        self.config(style='k.TCombobox', state='readonly', font=fo)

        # self.config(style='k.TCombobox', state='readonly')
        # self.config(style='k.TCombobox')


    def __str__(self) -> str:
        return """Para aplicar los estilos, use alt"""


if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    rz.config(bg='black')

    wg = KCombobox(rz)
    wg.items = ["uno", "dos", "tres", "cuatro", "cinco"]
    def muestra(e=None):
        print("elegido:: ", wg.currentIndex, wg.currentItem)
        #print("elegido:: no", e)
    wg.cmdSelected(muestra)
    wg.currentIndex = 2
    wg.setStyle()

    wg.grid(row=0, column=0, sticky='we')
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('Kombobox')
    rz.mainloop()