# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox

glavno_okno = Tkinter.Tk()

def klik_gumba():
    tekst = ""
    for i in range(1, int(vnos1.get()) + 1):
        if i % 3 == 0 and i % 5 == 0:
            vrstica = "FizzBuzz"
        elif i % 3 == 0:
            vrstica = "Fizz"
        elif i % 5 == 0:
            vrstica = "Buzz"
        else:
            vrstica = str(i)
        tekst += vrstica + "\n"
        tkMessageBox.showinfo("Izpis", tekst)

glavno_okno.title("FizzBuzz")
glavno_okno.geometry("400x500+500+200")

pozdrav = Tkinter.Label(glavno_okno, text="Pozdravljeni v FizzBuzzu!" + "\n")
pozdrav.config(font=("Verdana", 15, "bold"))
pozdrav.pack()

vnesi_st = Tkinter.Label(glavno_okno, text="Vnesite število med 1 in 100")
vnesi_st.config(font=("Arial", 10, "bold"))
vnesi_st.pack()

vnos1 = Tkinter.Entry(glavno_okno)
vnos1.pack()

gumb1 = Tkinter.Button(glavno_okno, text="Izvedi", command=klik_gumba)
gumb1.pack()

glavno_okno.mainloop()
