from ventana_reno import VentanaReno


if __name__ == '__main__':
    app = VentanaReno(bg="#212019", bg_bar='gray20')
    app.onTop(True)
    app.geometry("680x350")
    app.mainloop()