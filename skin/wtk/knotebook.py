from tkinter import ttk
import tkinter as tk


class KNotebook(ttk.Notebook):
    def __init__(self, parent, *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self._config_KNotebook()
        
    def _config_KNotebook(self):
        self.pag1 = tk.Frame(self, bg='yellow')
        self.pag2 = tk.Frame(self)
        
        style = ttk.Style()
        style.layout('TNotebook.Tab', [])
        
        self.add(self.pag1)
        self.add(self.pag2)
        #self.segundo()
    
    def primero(self):
        self.select(0)
        
    def segundo(self):
        self.select(1)
        

if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    wg = KNotebook(rz)
    wg.grid(row=0, column=0, sticky='wens')
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('KNotebook')
    rz.mainloop()