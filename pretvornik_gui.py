# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox

glavno_okno = Tkinter.Tk()

def klik_gumba_km():
    try:
        if vnos1.get():
            milje = float(vnos1.get()) * 0.62137
            tkMessageBox.showinfo("Rezultat", str(milje) + " " + "milj")
    except ValueError:
        tkMessageBox.showerror("Napačen vnos", "Napačen vnos, vnesite številko.")

def klik_gumba_milje():
    try:
        if vnos2.get():
            km = float(vnos2.get()) * 1.609344
            tkMessageBox.showinfo("Rezultat", str(km) + " " + "kilometrov")
    except ValueError:
        tkMessageBox.showerror("Napačen vnos", "Napačen vnos, vnesite številko.")


glavno_okno.title("Pretvornik enot")
glavno_okno.geometry("400x500+500+200")

pozdrav = Tkinter.Label(glavno_okno, text="Pozdravljeni v pretvorniku enot!" + "\n")
pozdrav.config(font=("Verdana", 15, "bold"))
pozdrav.pack()

#kilometri
vnesi_km = Tkinter.Label(glavno_okno, text="Vnesite kilometre (samo številko): ")
vnesi_km.config(font=("Arial", 10, "bold"))
vnesi_km.pack()

vnos1 = Tkinter.Entry(glavno_okno)
vnos1.pack()

gumb1 = Tkinter.Button(glavno_okno, text="Pretvori v milje", command=klik_gumba_km)
gumb1.pack()

#milje
vnesi_milje = Tkinter.Label(glavno_okno, text="Vnesite milje (samo številko): ")
vnesi_milje.config(font=("Arial", 10, "bold"))
vnesi_milje.pack(pady=(30, 0))

vnos2 = Tkinter.Entry(glavno_okno)
vnos2.pack()

gumb2 = Tkinter.Button(glavno_okno, text="Pretvori v kilometre", command=klik_gumba_milje)
gumb2.pack()


glavno_okno.mainloop()
