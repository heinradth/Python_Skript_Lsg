# Eine Funktion "foo(number)" die eine ganze Zahl nimmt
# und überprüft, ob diese positiv, negativ ungerade oder
# gar kein Integer ist.

def foo(number):

    number_dict = {}

    if number < 0:
        number_dict["vorzeichen"] = "negativ"
    else:
        number_dict["vorzeichen"] = "positiv"

    if type(number) is int:
        if number % 2 == 0:
            number_dict["parität"] = "gerade"
        else:
            number_dict["parität"] = "ungerade"
    else:
        number_dict["parität"] = "kein Integer"

    return number_dict


print(foo(90))
print(foo(-3))
print(foo(-44.3))
