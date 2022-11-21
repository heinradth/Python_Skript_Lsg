from K15_A1 import Haus


def print_haus(h):
    print("Adresse:", h.strasse, h.hausnummer)
    print("Farbe:", h.farbe)
    print("Preis: ", h.preis, "€", sep="")
    print("Stockwerke:", h.stockwerkanzahl)
    print("Wohnfläche: ", h.qm, "qm", sep="")
    print("")


if __name__ == "__main__":
    mein_haus = Haus("Hauptstraße", 1, "weiß", 25483562315484651, 2, 13)
    print_haus(mein_haus)
