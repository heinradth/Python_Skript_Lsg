def is_included(some_string):
    if "funktioniert" in some_string:
        return True
    else:
        return False


string_1 = "Das funktioniert so nicht!"
string_2 = "Dat funzt so nich,"

print(is_included(string_1))
print(is_included(string_2))