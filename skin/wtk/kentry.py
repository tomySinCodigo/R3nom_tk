from tkinter import ttk
import tkinter as tk


class KEntry(ttk.Entry):
    def __init__(self, parent, *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self._config_KEntry()
        
    def _config_KEntry(self):
        self.TEXTO = tk.StringVar()
        self.config(textvariable=self.TEXTO)
        
    def get(self):
        self.TEXTO.get()
        
    def text(self, texto:str):
        self.TEXTO.set(texto)
        
    def estilo(self, s:str, bg='black', fg='orange'):
        s.configure(
            'k.TEntry',
            fieldbackground=bg,
            foreground=fg,
            insertcolor=fg,
            insertwidth=2,
            bordercolor=bg,
            borderwidth=0,
            relief='flat',
            selectborderwidth=0,
            selectforeground=bg,
            selectbackground=fg
        )
        self.config(style='k.TEntry')
        

if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    
    wg = KEntry(rz)
    wg.grid(row=0, column=0, sticky='wens')
    
    ss = ttk.Style()
    ss.theme_use('alt')
    wg.estilo(ss)
    
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('KEntry')
    rz.mainloop()