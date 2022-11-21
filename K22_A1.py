from tkinter import *
from tkinter.ttk import *


def btnFar_click():
    form["bg"] = "red"


form = Tk()
form.title("Hauptfenster")
form.wm_geometry("400x200")

# Label und Button hinzufügen
lbl = Label(form, text="K22_A1")
lbl.place(x=150, y=80)
btnFar = Button(form, text="Färben", command=btnFar_click)
btnFar.place(x=150, y=100)

# Endlossscheife zum Starten des Fensters
form.mainloop()
