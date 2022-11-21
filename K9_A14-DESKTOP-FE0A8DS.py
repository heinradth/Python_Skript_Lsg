# A13 erweitern mit 50€, 10€ und 5€ Scheinen
# und 2€ und 1€ Münzen
# 2 Varianten:
#   1: Möglichst wenig Scheine und Münzen
#   2: Scheine und Münzen möglichst gleichmäßig

def wechselautomat(geld):
    rest = geld
    while True:
        print("1.Variante: Möglichst wenig Scheine und Münzen.")
        print("2.Variante: Scheine und Münzen möglichst gleichmäßig.")
        var = int(input("Wähle eine Variante(1 oder 2): "))
        if var == 1:
            schein50 = rest // 50
            rest -= schein50 * 50
            schein20 = rest // 20
            rest -= schein20 * 20
            schein10 = rest // 10
            rest -= schein10 * 10
            schein5 = rest // 5
            rest -= schein5 * 5
            muenze2 = rest // 2
            rest -= muenze2 * 2
            muenze1 = rest

            print("Ausgabe: ")
            print(schein50, "x 50€", sep="")
            print(schein20, "x 20€", sep="")
            print(schein10, "x 10€", sep="")
            print(schein5, "x 5€", sep="")
            print(muenze2, "x 2€", sep="")
            print(muenze1, "x 1€", sep="")
            break

        elif var == 2:
            schein50 = rest * 0.65 // 50
            rest -= schein50 * 50
            schein20 = rest * 0.65 // 20
            rest -= schein20 * 20
            schein10 = rest * 0.65 // 10
            rest -= schein10 * 10
            schein5 = rest * 0.7 // 5
            rest -= schein5 * 5
            muenze2 = rest * 0.7 // 2
            rest -= muenze2 * 2
            muenze1 = rest

            print("Ausgabe: ")
            print(schein50, "x 50€", sep="")
            print(schein20, "x 20€", sep="")
            print(schein10, "x 10€", sep="")
            print(schein5, "x 5€", sep="")
            print(muenze2, "x 2€", sep="")
            print(muenze1, "x 1€", sep="")
            break

        print("Diese Variante gibt es nicht!")


wechselautomat(500)
