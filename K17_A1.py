# Denk dir ne Aufgabe selbst aus die irgendwas
# mit den Klassen hier macht...
# Kreative Aufgabenstellung: 0/5 Sternen.

class Fahrzeug:
    def __init__(self, raeder, sitze, ps, verbrauch) -> None:
        self.raeder = raeder
        self.sitze = sitze
        self.ps = ps
        self.verbrauch = verbrauch


class Motorrad(Fahrzeug):
    def __init__(self, raeder, sitze, ps, verbrauch, wurstblinker):
        super().__init__(raeder, sitze, ps, verbrauch)
        self.wurstblinker = wurstblinker


class Auto(Fahrzeug):
    def __init__(self, raeder, sitze, ps, verbrauch, becherhalter):
        super().__init__(raeder, sitze, ps, verbrauch)
        self.becherhalter = becherhalter
