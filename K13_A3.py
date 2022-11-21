def read_one_value(text_data):
    for row in text_data:
        values = row.split(",")
        for value in values:
            print(value)


with open("K13_A1.txt", "r") as data:
    read_one_value(data)
    data.close()

