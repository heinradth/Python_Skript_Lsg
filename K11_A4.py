def hauptstaedte():

    hs_dict = {}
    index = 1

    while True:
        land = str(index) + ". "
        land += input("Land: ")
        hs_dict[land] = input("Hauptstadt: ")
        index += 1
        print("Weitermachen? (j/n): ")
        if input() == "n":
            break

    print("     Land\t\t|   Hauptstadt   ")
    for stadt in hs_dict:
        print(stadt, "\t|   ", hs_dict[stadt])


hauptstaedte()
