from cores.corex import CoreX


if __name__ == '__main__':
    com = "[$duracion$ $bitratev$ $modelos$]-$alto$p"
    vd = "C:/Users/mortadela/Downloads/7276517264029.mp4"

    cx = CoreX(com, vd)
    # print(cx.getArg())
    res = cx.useFFmpeg()
    print(res)