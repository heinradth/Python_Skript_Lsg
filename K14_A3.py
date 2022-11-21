def super_fun(number):
    for i in range(number):
        filename = "file" + str(i + 1) + ".txt"
        with open(filename, "w") as data:
            data.close()


# Mit Vorsicht geniessen!
# Antwort lautet ja, es werden 9999 Dateien erstellt.
# super_fun()
