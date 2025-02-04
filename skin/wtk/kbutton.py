from tkinter import ttk
import tkinter as tk


class KButton(ttk.Button):
    def __init__(self, parent, *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self._config_KButton()
        
    def _config_KButton(self):
        ...
        
    def estilo(
        self, s:str, fg='orange', bg='gray20',
        fgp='white', bgp='black',
        fo=("Consolas", 10, 'normal'),
        fga='gray20', bga='orange'
    ):
        """fg, bg, [fgp, bgp]pressed, [fga, bga]active"""
        s.configure(
            "k.TButton",
            background=bg, foreground=fg,
            relief='flat', highlightthickness=0,
            borderwidth=0, font=fo,
            highlightcolor='red'
        )
        s.map(
            "k.TButton",
            background=[('pressed', bgp), ('active',bga)],
            foreground=[('pressed', fgp), ('active',fga)],
            #relief=[('pressed', 'raised'), ('!pressed', 'flat')]
            #relief=[('active', 'sunken'), ('!active', 'flat')]
        )
        self.config(style="k.TButton")
        

if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    
    ss = ttk.Style()
    ss.theme_use('alt')
    
    wg = KButton(rz, text="mi botn")
    wg.estilo(ss)
    wg.grid(row=0, column=0, sticky='wens')
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('KButton')
    rz.mainloop()