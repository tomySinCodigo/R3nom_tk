import tkinter as tk
from mi_ventana.frame_botones import FrameBotones


class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("300x100")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        wg = FrameBotones(self)
        wg.grid(row=0, column=0, sticky="wens")
        

if __name__=="__main__":
    app = Ventana()
    app.mainloop()

