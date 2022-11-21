# Eine Funktion die alle möglichen Kombinationen
# für ein Turnier 1v1 ermittelt aus einer gegebenen Anzahl an Spielern.
# Doppelungen sollen ausgeschlossen werden.

def all_combinations(playernumber):
    for i in range(1, playernumber + 1):
        for j in range(i + 1, playernumber + 1):
            print("Player ", i, "vs", j, sep="")


all_combinations(4)
