# Keine echte Aufgabe. Ist nur drin, weil ich das so wollte.

from K18_A1 import Mage, Warrior


def introduction(creature):
    creature.introduction()


mag_obj = Mage(140, "Gandalf", "200", 9)
war_obj = Warrior(200, "Aragorn", "190", 4)

introduction(mag_obj)
introduction(war_obj)
