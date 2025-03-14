from tkinter import ttk
import tkinter as tk
from pathlib import Path
from typing import Iterable


class Iconos:
    def __init__(self):
        self.dc = {
            'folder':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAA3UlEQVR4nO2PMWoCURCGv3kuAUUwEFDPkc4z+Fgrq
        wgpcgFDbAKCB8glcgFh1bXSyibdegQrC7cwCaQR4psUQbMkwi4BsfErf+b/ZgZOjWivZ+LrqKbq8rvQGFmX/TDKJIiD+hMinWSoq
        ANzV2mMntMFAztBWV54er8LN1segEdU3v8U0Ddn5Kbqhy8A3vdGNpd2/JqY666Gdm7Qq98Ch7SN0xbwIzhExQ/7h/J4YJuK7Hsm7
        cc0zgLwFBYCt6vANrMUFIqITveCT6Gdw81ySCGLwCnrcukj+OfBR+ALCj9DJGXIwrsAAAAASUVORK5CYII=''',
            'video':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABt0lEQVR4nJWTMW9TQRCEv7n3HCMEKBIdQfZzSIFSB5
        QGkoKeAomCIv+Dipo/wE+giEQbJAggUSHRoihEgdgmiBYESmL73Q2F/YJNLGSm2lvtze3O7IkKtkCAoQok8z9YsuuP7DBGmjF+ng
        INCz/MNbiwAbQgnATScYKtroqdUyJI0zoSQOHuGmg1ET8Fws9Eump8SbgM8KKtxY+nRFI8Q9D0wUMT3nfV3K4KG3TWA2nFqMzQbq
        C5vS/1sANSqggCQCLMm/IEb2ZNH5xDil0Vr9pafFyidsS3enTvXvHhZaQ0FHyMQHguECK6HwuKEluVgF9VPOuTnojBakb/zpL36t
        U9/gQpMfJvOJiMFEevhW+61jW1p5DNH1FbRoqVO/+06CyS/s6MCJxVgo5EPB0BKRX+3BSDByb+OM9gB29mlZA5gMn7psyxszbtHL
        VKIAIsuH3P+KapvYscv97X9d64iPmoje8mqyHFDkTsvMHhbYgrQDJ6W6ex/WWKjdUerAvdSGQHovxltGB0UcQo9LKj1u5otOmLhL
        fqDZY3IBSQTkQ8MtnzWVZ5Amt+k08kZv5MlfKT+Zm+82880963ILge2wAAAABJRU5ErkJggg==''',
        }
        self.ICONOS = []
        
    def get(self, nom:str) -> str:
        icono = self.dc.get(nom)
        self.ICONOS.append(icono)
        return icono


class KTreeview(ttk.Treeview):
    def __init__(self, parent, bg="gray10", *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self.bg = bg
        self._config_KTreeview()
        
    def _config_KTreeview(self):
        self.config(show='tree')
        self.icos = Iconos()
        self.DATA = {}
        self.OPEN = True
        
    def setStyle(
        self, s:str=None, fg="gray60", bg="gray20", fo=("Consolas", 10, "normal"),
        fge='azure', bge='black'
    ):
        if not s:
            s=ttk.Style()
            s.theme_use('default')

        s.configure(
            'k.Treeview',
            foreground=fg,
            # background=bg,
            background=self.bg,
            fieldbackground=bg,
            relief='flat',
            borderwidth=0,
            Highlightcolor=bg,
            Highlightthickness=0,
            padding=0,
            bd=0,
        )
        s.map(
            'k.Treeview',
            background=[('selected', bge)],
            foreground=[('selected', fge)]
        )
        s.layout(
            'k.Treeview',
            [('Treeview.treearea', {'sticky':'wens'})]
        )
        self.config(style='k.Treeview')
        
    def clear(self):
        self.delete(*self.get_children())
        
    def setItems(self, rutas:Iterable):
        # ICONOS
        self.icono_folder = tk.PhotoImage(data=self.icos.get('folder'))
        self.icono_video = tk.PhotoImage(data=self.icos.get('video'))
        # ICONOS
        self.clear()
        self.folder = Path(rutas[0]).parent
        rz = self.insert(
            '', 'end', text=self.folder.name,
            image=self.icono_folder
        )
        for archivo in rutas:
            r = Path(archivo)
            name = r.name
            self.insert(rz, 'end', text=name, image=self.icono_video)
            self.DATA[f'{name}'] = {
                'r':r.as_posix(),
                'folder':Path(r.parent).as_posix(),
                'name':name,
                'stem':r.stem,
                'suffix':r.suffix
            }
        self.item(rz, open=True)
        
    @property
    def currentItem(self):
        # return self.item(self.currentIndex(), 'text')
        texto = self.item(self.currentIndex(), 'text')
        if texto in self.DATA:
            return self.DATA[texto]
        return None
        
    def currentIndex(self):
        return self.selection()[0]
        
    def cmdSelect(self, metodo):
        self.bind('<<TreeviewSelect>>', metodo)
        
    def expand(self):
        for item in self.get_children():
            self.item(item, open=True)
            
    def colapse(self):
        for item in self.get_children():
            self.item(item, open=False)
    
    def setExpand(self, b:bool=True):
        self.expand() if b else self.colapse()
            
    def toggle(self):
        self.colapse() if self.OPEN else self.expand()
        self.OPEN = not self.OPEN

    def getItems(self) -> list:
        """retorna [{indice, texto, parent}, {...}]"""
        indices_folders = self.get_children('')
        res = []
        for item in indices_folders:
            texto = self.item(item, 'text')
            res.append({
                'indice':item, 'texto':texto,
                'parent':'', 'data':''
            })
            subitems = self.get_children(item)
            for subitem in subitems:
                subitem_tex = self.item(subitem, 'text')
                res.append({
                    'indice':subitem, 'texto':subitem_tex,
                    'parent':item, 'data':self.DATA[subitem_tex]
                })
        return res
    
    def setCurrentIndex(self, i=0):
        items = self.getItems()
        self.selection_set(items[i].get('indice'))


        

if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    #rz.config(background="red")
    
    # ss = ttk.Style()
    # ss.theme_use('alt')
    
    wg = KTreeview(rz)
    # wg.estilo(ss, bg='#202220')
    wg.setStyle(bg='#202220')
    wg.grid(row=0, column=0, sticky='wens')
    li = ['D:/bta/tkinter_pro/ttk/nb3.py', 'D:/bta/tkinter_pro/ttk/gastos1.py']
    wg.setItems(li)
    
    def muestra(e=None):
        nom = wg.currentItem
        if nom:
            print('nom :: ', nom)

        # if nom in wg.DATA:
        #     res = wg.DATA[nom]
        #     print(res.get('r'))
        #     rz.title(nom)
        
    
    wg.cmdSelect(muestra)
    # obteniendo items
    from pprint import pprint
    # pprint(wg.getItems())
    wg.setCurrentIndex(1)

    
    btn_op = ttk.Button(rz, text="toggle", command=wg.toggle)
    btn_op.grid(row=1, column=0, sticky="wens")
    
    
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('KTreeview')
    rz.mainloop()