from K15_A1 import Haus
from K15_A2 import print_haus


haus_1 = Haus("Hauptstraße", 1, "weiß", 2123333, 2, 13)
haus_2 = Haus("Lange Straße", 3, "weiß", 4434, 2, 1)
haus_3 = Haus("Andere Straße", 5, "weiß", 1212121212, 2, 132)

dorf = [haus_1, haus_2, haus_3]

for haus in dorf:
    print_haus(haus)
print("________________________________")

haus_1.preis = -300
for haus in dorf:
    print_haus(haus)
print("________________________________")

haus_1.preis = 2
haus_1.qm = 20
for haus in dorf:
    print_haus(haus)

