from tkinter import ttk
import tkinter as tk


class MiScroll(ttk.Scrollbar):
    def __init__(self, parent=None, bg='white', fg='#3E56D3', s='scr', *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self.bg = bg
        self.fg = fg
        self.estilo = s
        self._config_MiScroll()

    def _config_MiScroll(self):
        bg, fg = self.bg, self.fg
        self.ss = ttk.Style()
        self.ss.theme_use('clam')
        self.ss.configure(
            f'{self.estilo}.Vertical.TScrollbar',
            gripcount=0,
            background=fg,
            darkcolor=fg,
            lightcolor=fg,
            troughcolor=bg,
            bordercolor=bg,
            relief='flat',
        )
        self.ss.map(
            f'{self.estilo}.Vertical.TScrollbar',
            background=[('!active', bg), ('active', fg)],
            arrowcolor=[('active', bg), ('!active', fg)]
        )
        self.config(style=f'{self.estilo}.Vertical.TScrollbar')


class MiTexto(tk.Frame):
    def __init__(self, parent=None, *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self._config_MiTexto()

    def _config_MiTexto(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.tex = tk.Text(
            self,
            bg=self.color('bg'),
            fg=self.color('fg'),
            padx=8, pady=5,
            insertbackground=self.color('fg'),
            selectbackground=self.color('select bg'),
            selectforeground=self.color('select fg'),
            font=('Lucida Console', 8, 'normal'),
            relief='flat',
            border=0,
            #wrap='word',
        )
        self.tex.grid(row=0, column=0, sticky='wens', padx=4)
        self.config(bg=self.color('bg'))
        self._coloca_scroll()

    def color(self, nom):
        self.colores = {
            'bg':'#191C21',
            'fg':'white',
            'select bg':'black',
            'select fg':'orange',
            'scroll bg':'gray10',
            'scroll fg':'gray'
        }
        return self.colores.get(nom)

    def msg(self, texto, tag='_tg', fg=None, bg=None, **kwargs):
        self.tex.insert('end', texto, (texto, tag))
        if fg:
            self.tex.tag_config(tag, foreground=fg, **kwargs)
        if bg:
            self.tex.tag_config(tag, background=bg, **kwargs)

    def borrar_todo(self):
        self.tex.delete('0.1', 'end')

    def texto_a_clipboard(self, texto):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()

    def escribe(self, texto):
        self.tex.insert('end', texto)
        self.tex.see('end')

    def obten_texto(self):
        return self.tex.get('0.1', 'end').strip('\n')

    def al_final(self):
        self.tex.see('end')

    def _coloca_scroll(self):
        self.scroll = MiScroll(
            self, orient='vertical', command=self.tex.yview,
            bg=self.color('bg'),
            fg='#8DA399'
        )
        self.scroll.grid(row=0, column=0, sticky='ens')
        self.tex.config(yscrollcommand=self.scroll.set)

    def error(self, texto):
        d = {'font': 'Consolas 9 bold'}
        self.msg(' ERROR ', tag='errn', fg='white', bg='#DE003B', **d)
        self.msg(' ')
        self.msg(f"{texto}\n", tag='err_msg', fg='#FF6B74', **d)

    def error2(self, texto):
        d = {'font': 'Consolas 8 bold'}
        self.msg(' ! ', tag='errn2', fg='white', bg='#FF0353', **d)
        self.msg(' ')
        self.msg(f"{texto}\n", tag='err2_msg', fg='#FF6B74', **d)

    def cf(self, texto, i=6, **kw):
        colores = ['#606A85', '#798560', '#748B91', '#948B91', '#748B91', '#B1B878', '#FFC335']
        self.msg(f'{texto}', f'tg_{i}', colores[i], **kw)



if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    wg = MiTexto()
    wg.grid(row=0, column=0, sticky='wens')
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('MiTexto')

    wg.error('algo no va bien, no se eusand encontro algo con el directorio mencionado para la ejeucion del progra,a')
    wg.error2('No encontrado.')
    wg.cf('nombre carpeta UNO\n', i=6)
    wg.cf('nombre carpeta UNO\n', i=5)
    wg.cf('nombre carpeta UNO\n', i=3)
    wg.cf('segunda lineas\n', i=5)
    rz.mainloop()