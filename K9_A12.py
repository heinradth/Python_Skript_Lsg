# D&D Kampf zwischen zwei Spielern abbilden.
# Drei Klassen zur Auswahl: Krieger, Magier, Schurke
# Spieler mit höherem Initiativewert (random) fängt an
# Spieler greifen sich abwechselnd an bis einer keine LP mehr hat
# Nachricht welcher Spieler gewonnen hat

from random import randint


krieger = {
    # ____Grundwerte____
    "Initative":         [1, 8],
    "Lebenspunkte":      10,

    # ____Fähigkeiten____
    "Schwertschlag":     [1, 7],
    "Schildblock":       [1, 4], # reduziert nächsten feindl. Angriff
    "Heiltrank":         [1, 6]  # nur 1x
}

magier = {
    # ____Grundwerte____
    "Initative":         [1, 6],
    "Lebenspunkte":      6,

    # ____Fähigkeiten____
    "Feuerball":         [2, 7],  # lädt eine Runde, macht Schaden nächste Runde
    "Arkaner_Pfeil":     [1, 6],
    "Spiegelbilder":     [1, 2],  # hält 2 Runden
    "Kleine_Heilung":    [1, 4]   # nur 1x
}

schurke = {
    # ____Grundwerte____
    "Initative":         [1, 10],
    "Lebenspunkte":      8,

    # ____Fähigkeiten____
    "Hinterhalt":        [1, 3],  # Passiv: falls höhere Ini. + auf Angriff
    "Dolchangriff":      [2, 4],
    "Schmutz":           [1, 2],  # wenn Treffer, nächster feindl. Angriff keinen Schaden
    "Heiltrank":         [1, 4]   # nur 1x
}

klassen = {
    "Krieger": krieger,
    "Magier": magier,
    "Schurke": schurke
}


# Berechnen des Würfelwurfs
def roll(wurf):
    x = 0
    for i in range(wurf[0]):
        x += randint(1, wurf[1])
    return x


# Anzeigen der restlichen Lebenspunkte
def show_lp(pl1, pl2):
    print("Spieler 1:", pl1[0], "LP")
    print("Spieler 1:", pl2[0], "LP")


# Rundenablauf
def runde(pl1, pl2):
    print("___Kampfrunde___")
    print("Wurf um Initiative: ")
    while True:
        i1 = roll(pl1[1]["Initiative"])
        i2 = roll(pl1[1]["Initiative"])
        if i1 == i2:
            continue
        break
    print("Spieler 1:", i1, "\nSpieler 2:", i2)
    if i1 > i2:
        print("Spieler 1 beginnt.")
        print("Wähle eine Fähigkeit: ")
    else:
        print("Spieler 2 beginnt.")


# Klassenauswahl der zwei Spieler
def player_select():
    print("Verfügbare Klassen:   Krieger   Magier   Schurke\n")
    print("\n 1.Spieler")
    while True:
        fst_player = input("Wähle eine Klasse: ")
        if fst_player != "Krieger" and fst_player != "Magier" and fst_player != "Schurke":
            print("Diese Klasse gibt es nicht!")
            continue
        break

    print("\n 2.Spieler")
    while True:
        sec_player = input("Wähle eine Klasse: ")
        if sec_player != "Krieger" and sec_player != "Magier" and sec_player != "Schurke":
            print("Diese Klasse gibt es nicht!")
            continue
        break

    return [fst_player, sec_player]


# Fähigkeiten
def heiltrank(pl):
    if pl[2] > 0:
        pl[2] -= 1
        pl[0] += roll([1, 6])
        if pl[0] > pl[1]["Lebenspunkte"]:
            pl[0] = pl[1]["Lebenspunkte"]
    else:
        print("Heiltränke leer!")


def schwertschlag(pl):
    return roll([1, 7])


def schildblock(pl):
    pl[3] += roll([1, 4])


def feuerball(pl):
    if pl[4] >= 1:
        print("Feuerball bereit!")
        return roll([2, 7])
    else:
        pl[4] += 1
        print("Feuerball lädt auf...")


def arkaner_pfeil(pl):
    return roll([1, 6])


def kleine_heilung(pl):
    if pl[2] > 0:
        pl[2] -= 1
        pl[0] += roll([1, 4])
        if pl[0] > pl[1]["Lebenspunkte"]:
            pl[0] = pl[1]["Lebenspunkte"]
    else:
        print("Heilung bereits verbraucht!")


def spiegelbilder(pl):
    print()


def dolchangriff(pl):
    print()


players = player_select()

# Spieler = [Lebenspunkte, Klasse, Anzahl Heiltränke, Rüstung, Rundenzähler]
player_one = [klassen[players[0]]["Lebenspunkte"], klassen[players[0]], 1, 0, 0]
player_two = [klassen[players[1]]["Lebenspunkte"], klassen[players[1]], 1, 0, 0]

