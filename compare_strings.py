def compare_strings(string1, string2):
    list = ""
    for letter1, letter2 in zip(string1, string2):
        if letter1 == letter2:
            list += "*"
        else:
            list += "."
    return list
    pass
