from cores.mi_tiempo import MiTiempo
from cores.FFmpeg.ffdata import FFData


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
        data = self.getFF()
        for arg in self.getArg():
            if arg in data:
                self.template = self.template.replace(f"${arg}$", str(data.get(arg)))
        return self.template

