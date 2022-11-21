# Funktion "wechselautomat(geld)"
# Gerader Betrag x wir dübergeben
# Betrag X wird in 20€-Scheinen und 1€ Stücken
# ausgegeben, mit möglichst wenigen Münzen

def wechselautomat(geld):
    scheine = geld // 20
    muenzen = geld - (scheine * 20)
    print(scheine, "x 20€ Scheine und ", muenzen, "x 1€ Münzen", sep="")
    return [scheine, muenzen]


wechselautomat(55)
