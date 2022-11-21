# Mach nen Quicksort-Algorithmus und such dir alles im Internet selbst dazu...
# Warum komme ich überhaupt noch zur Schule?
# Einfach nur Kann-Listen weitergeben und machen lassen. Wäre doch viel einfacher.

def partition(my_list, low, high):
    pivot = my_list[high]
    i = (low - 1)

    for j in range(low, high):
        if my_list[j] < pivot:
            i += 1
            my_list[i], my_list[j] = my_list[j], my_list[i]

    my_list[i + 1], my_list[high] = my_list[high], my_list[i + 1]
    return i + 1


def quicksort(my_list, low, high):
    if low < high:
        pi = partition(my_list, low, high)
        quicksort(my_list, low, pi - 1)
        quicksort(my_list, pi + 1, high)


unsorted_list = [0, 2, 3, 68, 5, 34, 33, 3]
print(unsorted_list)

quicksort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list)


