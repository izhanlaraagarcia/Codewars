# Count characters in your string
# This is the result of the "Count characters in your string" 6 kyu exercise in Codewars, language used: Python
# Codewars
def count(string):

    count={}
    for i in string:
        count[i]=count.get(i,0) + 1
    
    return count
