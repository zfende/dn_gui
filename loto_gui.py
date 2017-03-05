# -*- coding: utf-8 -*-
import random
import Tkinter
import tkMessageBox


def loto_stevila():
    stevila = []
    while len(stevila) < int(vnos.get()):
        novo_stevilo = random.randrange(1, 51)
        if not novo_stevilo in stevila:
            stevila.append(novo_stevilo)

    loto_stevilke = sorted(stevila)
    tkMessageBox.showinfo("Vaše loto številke so:", loto_stevilke)

glavno_okno = Tkinter.Tk()
glavno_okno.title("LOTO generator")
glavno_okno.geometry("400x500+500+200")

pozdrav = Tkinter.Label(glavno_okno, text="Pozdravljeni v LOTO generatorju!" + "\n")
pozdrav.config(font=("Verdana", 15, "bold"))
pozdrav.pack()


vnesi_st = Tkinter.Label(glavno_okno, text="Vnesite koliko številk: ")
vnesi_st.config(font=("Arial", 10, "bold"))
vnesi_st.pack()

vnos = Tkinter.Entry(glavno_okno)
vnos.pack()

gumb = Tkinter.Button(glavno_okno, text="Izvedi", command=loto_stevila)
gumb.pack()

glavno_okno.mainloop()