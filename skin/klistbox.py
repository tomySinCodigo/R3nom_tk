import tkinter as tk
from tkinter import ttk


class KScroll(ttk.Scrollbar):
    def __init__(self, parent=None, **kw):
        super().__init__(master=parent, **kw)
        self.parent = parent
        self._configKScroll()

    def _configKScroll(self):
        self.st = ttk.Style()
        self.st.theme_use('default')
        bg = "black"
        fg = "gray20"
        self.st.configure(
            "k.Vertical.TScrollbar",
            gripcount=0,
            background=bg,
            darkcolor=bg,
            lightcolor=bg,
            troughcolor=fg,
            bordercolor=bg,
            relief='flat',
            arrowcolor=fg,
            borderwidth=0,
            thickness=2
        )
        self.st.map(
            "k.Vertical.TScrollbar",
            background=[('active',bg), ('!active',bg)],
            # arrowcolor=[("active",bg), ("!active",fg)]
        )
        self.config(style="k.Vertical.TScrollbar")


class KListbox(tk.Listbox):
    def __init__(self, parent, *args, **kw):
        super(KListbox, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self._configKListbox()

    def _configKListbox(self):
        self.var_items = tk.StringVar(value=[])

    def setStyle(
        self,
        bg='#1E1E1E', fg='#B5B39A'
    ):
        self.config(
            background=bg,
            foreground=fg,
            selectbackground=fg,
            selectforeground=bg,
            listvariable=self.var_items,
            selectmode='single',
            takefocus=False,
            highlightthickness=0,
            borderwidth=0,
            activestyle='none',
            justify='left',
            relief='flat',
            font=('Consolas', 10, 'normal'),
            border=2,
        )

    @property
    def items(self):
        return [self.get(i) for i in range(self.size())]
        # return list(self.get(0, tk.END))

    @items.setter
    def items(self, items:list):
        self.delete(0, tk.END)
        self.var_items.set(items)
        self.update()

    @property
    def currentItem(self):
        return self.get(self.curselection())

    @currentItem.setter
    def currentItem(self, item):
        self.selection_clear(0, tk.END)
        try:
            idx = self.items.index(item)
            self.selection_set(idx)
        except ValueError:
            pass
        self.update()

    def selectAll(self):
        self.selection_set(0, tk.END)

    def deselectAll(self):
        self.selection_clear(0, tk.END)

    def setScroll(self):
        self.scroll = KScroll(
            self, orient=tk.VERTICAL, command=self.yview
        )
        self.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def clear(self):
        self.delete(0, tk.END)

    def cmdSelect(self, metodo):
        self.bind('<<ListboxSelect>>', metodo)


if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry('400x120')
    wg = KListbox(vn)
    wg.grid(row=0, column=0, sticky='wens')
    wg.setStyle()
    wg.setScroll()
    wg.items = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
    wg.currentItem = 'tres'

    def elegido(self):
        print(wg.currentItem)
        # print(wg.items)

    wg.cmdSelect(elegido)


    vn.columnconfigure(0, weight=1)
    vn.rowconfigure(0, weight=1)
    vn.mainloop()