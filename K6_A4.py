print ("Text ohne if")

def schreibmehr ():
     print ("Text mit if")

if __name__ == "__main__":
    schreibmehr()

# Funktionen außerhalb der "if__name__=="__main__" Anweisung
# werden zwangsläufig beim Import ausgeführt.
# Innerhalb der Anweisung nur bei Aufruf.