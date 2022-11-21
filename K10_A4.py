# Selectionsort-Algorithmus, aber in-place arbeiten (nur eine Liste)

def sortieren(my_list):

    # Durchgehen der Liste nach Index
    for i in range(len(my_list)):
        smallest_int = my_list[i]
        index = 0

        # Ermitteln und Zuweisen des kleinsten Wertes in der Liste ab Index [i]
        for j in range(i, len(my_list)):
            if my_list[j] <= smallest_int:
                smallest_int = my_list[j]
                index = j

        my_list.pop(index)
        my_list.insert(i, smallest_int)
        
    return my_list


unsorted_list = [0, 2, 3, 1, 29, 22, 2, 0]

print(sortieren(unsorted_list))
