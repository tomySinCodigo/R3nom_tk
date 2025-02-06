from cores.FFmpeg.ffdata import FFData

class Tiempos:
    def ts_mseg(self, ts):
        '''retorna tiempo en int(mseg): 00:32:51.274 -> 1971274'''
        ho, mi, _ = ts.split(":")
        se, mz = _.split(".")
        horas = int(ho)*3.6e6
        minutos = int(mi)*6e4
        segundos = int(se)*1e3
        milisegundos = int(mz)
        return int(sum((horas, minutos, segundos, milisegundos)))
        
    def ts_seg(self, ts):
        '''retorna float(seg): 00:32:51.274 -> 1971.274'''
        mseg = self.timestamp_mseg(ts)
        return mseg/1e3
        
    def mseg_ts(self, milisegundos):
        '''retorna: {horas,minutos,segundos,milisegundos,tiempo,t}'''
        mseg = int(milisegundos)
        h, m ,s, z = self.mseg_hmsz(mseg)
        tiempo = f"{h:02d}:{m:02d}:{s:02d}.{z:03d}"
        t = tiempo[3::] if tiempo.startswith('00:') else tiempo
        return {
            'horas':h, 'minutos':m,
            'segundos':s, 'milisegundos':z,
            'tiempo':tiempo, 't':t
        }
        
    def mseg_hmsz(self, milisegundos):
        '''retorna tupla(int) =  h, m, s, z'''
        h, r = divmod(float(milisegundos), 3.6e6)
        m, r = divmod(r, 6e4)
        s, z = divmod(r, 1e3)
        return int(h), int(m), int(s), int(z)


class CoreFF:
    def readCmd(self, cmd:str):
        res = [p for p in cmd.split("$") if len(p)>3]
        return res


if __name__ == '__main__':
    # comando = "[$duracion$ $bitratev$ $modelos$]-$alto$p"
    # ff = CoreFF()
    # archivo = "C:/Users/mortadela/Downloads/7276517264029.mp4"
    # print(ff.readCmd(comando))

    # 'duration': '1687.360000',
    # 'duration_ts': 21598208,
    tt = Tiempos()
    # t = float('21598208')
    t = float('1687.360000')*1000
    # print(tt.mseg_hmsz(t))

    # import time

    # # Milisegundos de entrada
    # milisegundos = t

    # # Convertir milisegundos a segundos
    # segundos = milisegundos * 1000

    # # Usar time.gmtime para obtener la estructura de tiempo
    # estructura_tiempo = time.gmtime(segundos)

    # # Formatear solo la parte del tiempo (HH:MM:SS)
    # solo_tiempo = time.strftime("%H:%M:%S", estructura_tiempo)

    # print("Tiempo:", solo_tiempo)

    def aTiempo(frame):
        if frame < 3600000:
            m = int(frame/60000)
            s = int((frame - m*60000)/1000)
            li = [m, s]
        else:
            h = int((frame/3600000))
            # print('h: ', h)
            m = int((frame - h*3600000)/60000)
            # print('m: ', m)
            s = int((frame - (h*3600000 + m*60000))/1000)
            # print('s:', s)
            li = [h, m, s]
        return li
    
    print(aTiempo(t))
