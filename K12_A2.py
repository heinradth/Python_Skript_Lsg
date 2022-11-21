def nur_ungerade(some_list):
    ungerade = [x for x in some_list if x % 2 == 1]
    return ungerade


liste_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
liste_2 = [1523423, 2131523214, 214353546, 34532421, 2]

print(nur_ungerade(liste_1))
print(nur_ungerade(liste_2))