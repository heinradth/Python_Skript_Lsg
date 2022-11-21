# Eine Funktion "supersearch(d, value)", welche ein Dictionary(d)
# nach einem bestimmten Wert(Value) absucht. (Nicht KEY!)
# Gibt True oder False aus.
# d.get() ist nicht erlaubt.

def supersearch(d, value):
    for key in d:
        if d[key] == value:
            return True

    return False


wochentage = {
    1: "Montag",
    2: "Dienstag",
    3: "Meine Kerle"
}

print(supersearch(wochentage, "Montag"))
print(supersearch(wochentage, "ffffff"))
