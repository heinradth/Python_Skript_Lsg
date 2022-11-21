def my_numbers():
    numbers = [x for x in range(1, 11)]
    with open("my_first_numbers.csv", "w") as data:
        print(*numbers, sep=",", file=data)


my_numbers()
