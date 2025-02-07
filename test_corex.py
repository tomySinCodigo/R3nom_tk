from cores.corex import CoreX


if __name__ == '__main__':
    com = "[$duracion$ $bitratev$ $modelos$]-$alto$p"
    vd = "C:/Users/mortadela/Downloads/7276517264029.mp4"

    cx = CoreX(com, vd)
    # print(cx.getArg())
    res = cx.useFFmpeg()
    print(res)

    # res = cx.getMi()
    # print(res)

    # print(cx.useMediaInfo())

    # a = '3789kbps'
    # def uno(valor):
    #     num = int(valor.replace("kbps", ""))
    #     return f'{round(num/1e3, 2)}mb'
    
    # print(uno(a))