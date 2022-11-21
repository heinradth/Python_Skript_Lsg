def just_eighteen(text_data):
    for row in text_data:
        values = row.split(",")
        if int(values[2]) < 18:
            continue
        else:
            for value in values:
                print(value)


with open("K13_A1.txt", "r") as data:
    just_eighteen(data)
    data.close()
