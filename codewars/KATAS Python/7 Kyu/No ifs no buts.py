# This is the result of the "No ifs no buts" 7 kyu exercise in Codewars, language used: Python
# Codewars
def no_ifs_no_buts(a, b):
    return {
        a==b: (f"{a} is equal to {b}"),
        a<b: (f"{a} is smaller than {b}"),
        a>b: (f"{a} is greater than {b}"),
    }[True]
