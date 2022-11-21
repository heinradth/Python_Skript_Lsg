# Algorythmus zum sortieren einer Liste

def sortieren(unsorted_list):
    sorted_list = []

    for i in range(len(unsorted_list)):
        smallest_int = unsorted_list[0]

        for j in unsorted_list:
            if j <= smallest_int:
                smallest_int = j

        sorted_list.append(smallest_int)
        unsorted_list.remove(smallest_int)

    return sorted_list


my_list = [0, 2, 3, 1, 29, 22, 2, 0]

print(sortieren(my_list))
