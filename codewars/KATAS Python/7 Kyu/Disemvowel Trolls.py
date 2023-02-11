# CodeWars
# Disemvowel Trolls Python
def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    none=""
    string_

    for x in string_:
        if x in vowels:
            string_=string_.replace(x,none)
    return string_ 