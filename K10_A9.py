# Funktion "blablub(lis, obj)" ist gegeben. Naja nur der Name der Funktion und seine Argumente....
# Was soll das gute Ding machen?
# Die Funktion nimmt das zweite Argument(obj) und überprüft,
# ob es bereits im ersten Argument(lis) enthalten ist.
# Falls nicht, wird das Objekt an die Liste angehängt.

def blablub(lis, obj):
    for elem in lis:
        if elem == obj:
            return
    lis.append(obj)


my_list = ["wadda", "hadden", "duden", "da"]

blablub(my_list, "duden")
print(my_list)

blablub(my_list, "?")
print(my_list)
