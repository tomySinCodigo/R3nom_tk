class Tiempos:
    def mseg_ts(self, milisegundos, text:bool=True) -> str | tuple:
        """retorna mseg a timestamp, text[True:str, False:tuple]"""
        h, r = divmod(float(milisegundos), 3.6e6)
        m, r = divmod(r, 6e4)
        s, z = divmod(r, 1e3)
        return f"{h:02.0f}:{m:02.0f}:{s:02.0f}.{int(z):03d}" \
        if text else tuple(map(int, [h,m,s,z]))
    
    def _ts_hmsz(self, ts:str) -> list:
        """retorna timestamp a list[h,m,s,z] en mseg"""
        h, m, _ = ts.split(':')
        s, z = _.split('.')
        hmsz = tuple(map(int, (h,m,s,z)))
        return [int(x*y) for x, y in zip(hmsz, [3.6e6, 6e4, 1e3, 1])]
    
    def ts_mseg(self, ts:str) -> float:
        """retorna timestamp a milisegundos"""
        return sum(self._ts_hmsz(ts))

    def _ms_hmsz(self, mseg:str) -> tuple:
        """retorna timestamp en una list[h,m,s,z] de int"""
        return self.mseg_ts(mseg, text=False)
    
    def ts_cut(self, ts:str) -> str:
        """retorna timestamp recortado"""
        h, m, s, _ = self._ms_hmsz(self.ts_mseg(ts))
        if h==0:
            t = f"{s:02d}s" if m==0 else f"{m:02d}.{s:02d}"
        else:
            t = f'{h:02d}.{m:02d}.{s:02d}'
        return t


class Con:
    def kbps_mbps(self, value:str) -> str:
        """retorna [valor]kbps a [valor]mbps"""
        if "kbps" in value and len(value)>6:
            num = int(value.replace("kbps", ""))
            value = f'{round(num/1e3, 2)}mbps'
        return value
    
    def unidad(self, bytes:int, mil=1e3) -> str:
        """retorna una lista con [valor, valor+unidad, unidad]"""
        n = float(bytes)
        for u in ["bt", "kb", "mb", "gb", "tb"]:
            if n < mil:
                return [f"{n:.2f}", f"{n:.2f}{u}", u]
            n /= mil
    

class Conversor:
    ...


if __name__ == '__main__':
    ms = '2421822'
    ts1 = '01:00:21.822'
    tim = Tiempos()
    # t1 = tim.mseg_ts(ms)
    # print(t1)
    # print(tim.ts_mseg(t1))
    # print(tim._ts_hmsz(t1))
    # print(tim._ms_hmsz(ms))

    # print(tim.ts_cut(ts1))

    # con = Con()
    # a = con.unidad(126974)
    # print('a :: ', a)


