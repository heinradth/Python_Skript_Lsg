# Es ist eine Liste gegeben bestehend aus Strings.
# Wenn gewisse Zeichen bzw. Zeichenketten in den jeweiligen
# Strings vorkommen, sollen diese ausgegeben werden.

passwords = ["ababa", "baab", "sdiopc", "ajkwei", "bab"]


def pw_check(password_list):
    for elem in passwords:
        if "ab" in elem or "ba" in elem:
            print(elem, end=" ")


pw_check(passwords)
