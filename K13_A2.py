def read_every_line(text_data):
    for row in text_data:
        print(row)


with open("K13_A1.txt", "r")as data:
    read_every_line(data)
    data.close()
