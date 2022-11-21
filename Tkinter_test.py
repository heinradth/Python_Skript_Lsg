from tkinter import *
from tkinter.ttk import *


def btnEnd_click():
    form.destroy()


form = Tk()
form.title("Hauptfenster")
form.wm_geometry("400x200")

# Label und Button hinzufügen
lbl = Label(form, text="Mein Label")
lbl.place(x=150, y=80)
btnEnd = Button(form, text="Beenden", command=btnEnd_click)
btnEnd.place(x=150, y=100)

# Endlossscheife zum Starten des Fensters
form.mainloop()
