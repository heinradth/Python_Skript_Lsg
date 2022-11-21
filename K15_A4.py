from K15_A1 import Haus
from K15_A2 import print_haus


mein_haus = Haus("Hauptstraße", 1, "weiß", 25483562315484651, 2, 13)
print_haus(mein_haus)

Haus.neuer_anstrich(mein_haus, "grün")
print_haus(mein_haus)
