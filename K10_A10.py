# Eine Funktion die eine Zahl nimmt und in 0.1 Schritten
# bis zu dieser Zahl zählt.

def print_it(x):
    for i in range(x * 10):
        print(round(i * 0.1, 1))


print_it(2)
