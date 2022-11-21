# Eine Funktion die den letzten Wert einer Liste ausgibt
# und falls diese leer ist, "Leere Liste" ausgibt

def last_elem(my_list):
    while my_list:
        return my_list[-1]
    return "Leere Liste"


liste_1 = ["Hello", "is", "it", "me", "you're", "looking", "for"]
liste_2 = []

print(last_elem(liste_1))
print(last_elem(liste_2))
