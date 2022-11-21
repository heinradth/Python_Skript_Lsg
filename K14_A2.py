def my_numbers():

    # Hier wird versucht das erste Zeichen aus der Datei zu lesen.
    # Ist dieser nicht vorhanden, muss die Datei leer sein und kann beschrieben werden.
    with open("my_first_numbers.csv", "r") as data:
        if data.read(1):
            print("CSV-Datei bereits beschrieben.")
            return
        data.close()

    numbers = [x for x in range(1, 11)]
    with open("my_first_numbers.csv", "w") as data:
        print(*numbers, sep=",", file=data)
        data.close()


my_numbers()
