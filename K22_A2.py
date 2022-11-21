from tkinter import *
from tkinter.ttk import *
from random import randint


def btnRand_click():
    btnRand.place(x=randint(0, 400), y=randint(0, 200))


form = Tk()
form.title("Hauptfenster")
form.wm_geometry("400x200")

# Label und Button hinzufügen
lbl = Label(form, text="K22_A2")
lbl.place(x=150, y=80)
btnRand = Button(form, text="Klick mich!", command=btnRand_click)
btnRand.place(x=150, y=100)

# Endlossscheife zum Starten des Fensters
form.mainloop()
