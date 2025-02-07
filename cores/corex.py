from cores.mi_tiempo import MiTiempo
from cores.FFmpeg.ffdata import FFData
from cores.mediainfo.mi_video import MiVideo


class CoreX:
    def __init__(self, template, video):
        self.mt = MiTiempo()
        self.template = template
        self.VIDEO = video

    def getArg(self):
        return [k for k in self.template.split("$") if len(k)>3]
    
    def getFF(self):
        ff = FFData(archivo=self.VIDEO)
        ff.getInfo()
        data = ff.getData()
        t = self.mt.mseg_ts(float(data["duracion"])*1e3).get("t")
        d = {
            "duracion":t.replace(":", ".")
        }
        data.update(d)
        return data
    
    def useFFmpeg(self):
        return self.use(self.getFF())

    def getMi(self):
        miv = MiVideo(video_ruta=self.VIDEO)
        miv.extrae_data()
        data = miv.basico()
        t = self.mt.mseg_ts(float(data["duracion ms"])).get("t")
        d = {
            "duracion":t.replace(":", "."),
            "bitratev":self.kbps_mb(data["bitratev"])
        }
        data.update(d)
        return data
    
    def kbps_mb(self, valor):
        if "kbps" in valor and len(valor)>6:
            num = int(valor.replace("kbps", ""))
            valor = f'{round(num/1e3, 2)}mb'
        return valor

    def useMediaInfo(self):
        return self.use(self.getMi())
    
    def use(self, data):
        txt = self.template.strip()
        for arg in self.getArg():
            if arg in data:
                txt = txt.replace(f"${arg}$", str(data.get(arg)))
        return txt
