class MiTiempo:
    def ts_mseg(self, ts:str) -> int:
        """retorna tiempo en int[mseg]: de 00:32:51.274 a 1971274"""
        ho, mi, _ = ts.split(":")
        se, mz = _.split(".")
        horas = int(ho)*3.6e6
        minutos = int(mi)*6e4
        segundos = int(se)*1e3
        milisegundos = int(mz)
        return int(sum((horas, minutos, segundos, milisegundos)))
    
    def ts_seg(self, ts:str) -> float:
        '''retorna float[seg]: 00:32:51.274 -> 1971.274'''
        return self.ts_mseg(ts)/1e3
    
    def mseg_ts(self, milisegundos) -> dict:
        '''retorna: {horas,minutos,segundos,milisegundos,tiempo,t}'''
        mseg = int(milisegundos)
        h, m ,s, z = self.mseg_hmsz(mseg)
        tiempo = f"{h:02d}:{m:02d}:{s:02d}.{z:03d}"
        tm = tiempo[3::] if tiempo.startswith('00:') else tiempo
        t = tm[:tm.index('.')]
        return {
            'horas':h, 'minutos':m,
            'segundos':s, 'milisegundos':z,
            'tiempo':tiempo, 'tm':tm, 't':t
        }
        
    def mseg_hmsz(self, milisegundos) -> tuple:
        '''retorna tupla[int] =  h, m, s, z'''
        h, r = divmod(int(milisegundos), 3.6e6)
        m, r = divmod(r, 6e4)
        s, z = divmod(r, 1e3)
        return int(h), int(m), int(s), int(z)
    

if __name__ == '__main__':
    mit = MiTiempo()
    mseco = "685676"
    a = mit.mseg_ts(mseco)
    print(a)
    tim =  a.get('tiempo')
    print(mit.ts_seg(tim))
    print(mit.ts_mseg(tim))