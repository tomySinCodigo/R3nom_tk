import tkinter as tk


class LabelMenu(tk.Label):
    def __init__(
        self, parent=None, icono='skin/mi_ventana/icos10/T.png',
        titulo=' PROGRAMA', compound='left',
        font=('Consolas', 8, 'bold'),
        bg="#101010", fg="#BEB9A9",
        *args, **kw
    ):
        super(LabelMenu, self).__init__(
            master=parent, text=titulo,
            compound=compound, font=font,
            bg=bg, fg=fg,
            *args, **kw
        )
        self.parent = parent
        self.icono = icono
        self.titulo = titulo
        self.bga = 'black'
        self.iconoTk(icono)
        self._config_Labelmenu()

    def _config_Labelmenu(self):
        self.config(
            image = self.icono_tk,
        )
        self.menu = tk.Menu(
            self, tearoff=False,
            activebackground=self.bga,
            font=('Consolas', 8, 'bold')

        )
        self.menu.add_command(label='uno')
        self.menu.add_command(label='dos', command=self.test_click)
        self.bind('<Button-1>', self.accion_logo)

    def asigna_icono(self, icono):
        self.ico_mn = tk.PhotoImage(file=icono)
        self.config(image=self.ico_mn)

    def iconoTk(self, icono:str):
        self.icono_tk = tk.PhotoImage(file=icono)

    def accion_logo(self, e):
        # COORDENADAS DE LA VENTANA
        wx, wy = self.winfo_rootx(), self.winfo_rooty()
        # print(wx, wy)
        # ancho y alto de label
        lb = e.widget
        lbw, lbh = lb.winfo_width(), lb.winfo_height()
        # print(lbw, lbh)
        # coordenadas del menu debajo del label
        x, y = wx, wy+lbh
        self.menu.tk_popup(x, y)

    def test_click(self):
        print("click - item")

    def asigna_icono(self, icono:str):
        self.iconoTk(icono)
        self.config(image=self.icono_tk)


class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("600x20")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        wg = LabelMenu(self)
        wg.grid(row=0, column=0, sticky="wens")
        

if __name__=="__main__":
    app = Ventana()
    app.mainloop()
