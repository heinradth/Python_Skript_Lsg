# Programm zur Kinositzverteilung
# Kinosaal besteht aus 6 Reihen mit je 9 Sitzplätzen.
# Loge besitzt 2 Reihen mit je 9 Sitzplätzen.
# Einige Sitze sollen zufallsgeneriert belegt werden.
# Sitzplan soll per Konsole optisch ausgegeben werden.

from random import randint


plaetze_pro_reihe = 9
anzahl_reihen_ks = 6
anzahl_reihen_lg = 2
x = 0

reihe = []
kinosaal = []
loge = []

# Sitzplätze pro Reihe
for i in range(plaetze_pro_reihe):
    reihe.append(0)

# Reihen pro Saal bzw. Loge
for i in range(anzahl_reihen_ks):
    kinosaal.append(reihe[:])

for i in range(anzahl_reihen_lg):
    loge.append(reihe[:])

# Zufällige Platzbelegung   0 = leer    1 = besetzt
for i in range(anzahl_reihen_ks):
    for j in range(plaetze_pro_reihe):
        kinosaal[i][j] = randint(0, 1)

for i in range(anzahl_reihen_lg):
    for j in range(plaetze_pro_reihe):
        loge[i][j] = randint(0, 1)


def platzbelegung(saal, name):
    print("\nPlatzbelegung für ", name, ":", sep="")
    print("|---------Leinwand--------|\n")
    for rei in saal:
        for pl in rei:
            if pl == 0:
                print("[ ]", end="")
            else:
                print("[X]", end="")
        print()


platzbelegung(kinosaal, "Kinosaal")
platzbelegung(loge, "Loge")
