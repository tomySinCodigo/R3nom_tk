from tkinter import ttk
import tkinter as tk


class KNotebook(ttk.Notebook):
    def __init__(self, parent, bg, *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self.BG = bg
        self._config_KNotebook()
        self.estilo()
        
    def _config_KNotebook(self):
        self.pag1 = tk.Frame(self, bg=self.BG)
        self.pag2 = tk.Frame(self, bg=self.BG)
        self.add(self.pag1)
        self.add(self.pag2)
        
        # ss = ttk.Style()
        # ss.theme_use('alt')
        # ss.layout('TNotebook.Tab', [])
        # ss.configure(
        #     "knb.TNotebook",
        #     background=bg,
        #     borderwidth=0,
        #     relief="flat",
        # )
        # ss.map(
        #     "knb.TNotebook",
        #     background=bg,
        # )
        
        # self.add(self.pag1)
        # self.add(self.pag2)
        # self.config(style="knb.TNotebook")


        # ss.theme_create(
        #     "knb", parent="alt", settings={
        #         ".":{
        #             "configure":{
        #                 "relief":"flat",
        #                 "background":"gray20"
        #             }
        #         }
        #     }
        # )
        # ss.theme_use("knb")

    def estilo(self):
        bg = self.BG
        ss = ttk.Style()
        ss.theme_use('alt')
        ss.layout('TNotebook.Tab', [])
        ss.configure(
            "knb.TNotebook",
            relief='flat',
            background=bg,
        )
        ss.map(
            "knb.TNotebook",
            background=bg,
            foreground=[('selected', bg)],
            expand=[("!selected", [1, 1, 1, 0])],
            bordercolor=bg
        )
        self.config(style='knb.TNotebook')

    
    def primero(self):
        self.select(0)
        
    def segundo(self):
        self.select(1)

        

if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    wg = KNotebook(rz, bg='skyblue')
    wg.grid(row=0, column=0, sticky='wens')
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('KNotebook')
    rz.mainloop()