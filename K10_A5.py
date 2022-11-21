# Bubblesort-Algorithmus in-place

def bubblesort(my_list):
    for j in range(1, len(my_list)):
        for i in range(len(my_list) - j):
            if my_list[i] >= my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    return my_list

unsorted_list = [0, 2, 3, 1, 6, 22, 2, 2, 0]

print(bubblesort(unsorted_list))
