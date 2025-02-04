from tkinter import ttk
import tkinter as tk
from typing import Iterable


class Kombobox(ttk.Combobox):
    def __init__(self, parent,*args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self._config_Kombobox()
        
    def _config_Kombobox(self):
        self.ELEMENTOS = []
        
    @property
    def items(self) -> Iterable:
        return self.ELEMENTOS

    @items.setter
    def items(self, lista:Iterable):
        self.ELEMENTOS = lista
        self.config(state='normal')
        self.config(values=self.ELEMENTOS, state='readonly')

    @property
    def elegido(self) ->str:
        return self.get()

    @elegido.setter
    def elegido(self, elem:str):
        self.set(elem)

    @property
    def indice(self) -> int:
        return self.current()

    @indice.setter
    def indice(self, i:int):
        self.current(i)

    def item(self, elem:str):
        valores = list(self['values'])
        valores.append(str(elem))
        self['values'] = valores

    def metodo(self, metodo):
        self.bind('<<ComboboxSelected>>', metodo)
        
    def estilo(self, s, fg='RoyalBlue1', bg='black', fgm='RoyalBlue1', bgm='black',fo=('Consolas',12,'normal')):
        s.configure(
            'scb.TCombobox',
            foreground=fg,
            background=bg,
            bordercolor=bg,
            borderwidth=0,
            arrowcolor=fg,
            relief='flat',
            selectbackground=bg,
            selectforeground=fg,
            takefocus=False,
        )
        s.map('scb.TCombobox',fieldbackground=[('readonly',bg)])
        self.option_add('*TCombobox*Listbox.background', bgm)
        self.option_add('*TCombobox*Listbox.foreground', fgm)
        self.option_add('*TCombobox*Listbox.selectBackground', fg)
        self.option_add('*TCombobox*Listbox.selectForeground', bg)
        #self.config(style='scb.TCombobox', state='readonly', font=fo)
        
        self.config(style='scb.TCombobox', state='readonly', font=fo)
        

    def __str__(self) -> str:
        return """Para aplicar los estilos, use alt"""
        

if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    wg = Kombobox(rz)
    ss = ttk.Style()
    ss.theme_use('alt')
    wg.estilo(ss)
    wg.items = ["uno", "dos", "tres", "cuatro", "cinco"]
    def muestra(e=None):
        print("elegido:: ", wg.indice, wg.elegido)
        #print("elegido:: no", e)
    wg.metodo(muestra)
    
    wg.indice = 2
    
    wg.grid(row=0, column=0, sticky='we')
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('Kombobox')
    rz.mainloop()