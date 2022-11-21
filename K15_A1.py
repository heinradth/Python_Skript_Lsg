class Haus:
    def __init__(self, strasse, hausnummer, farbe, preis, stockwerkanzahl, qm):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.farbe = farbe
        self._preis = preis
        self.stockwerkanzahl = stockwerkanzahl
        self._qm = qm

    # K15_A4
    def neuer_anstrich(self, fa):
        self.farbe = fa

    # K16_A1
    @property
    def preis(self):
        return self._preis

    @property
    def qm(self):
        return self._qm

    @preis.setter
    def preis(self, value):
        if value < 0:
            print("Negative Werte nicht erlaubt!")
        else:
            print("Setter für Preis wurde aufgerufen.")
            self._preis = value

    @qm.setter
    def qm(self, value):
        if value < 0:
            print("Negative Werte nicht erlaubt!")
        else:
            print("Setter für Quardatmeter wurde aufgerufen.")
            self._qm = value
