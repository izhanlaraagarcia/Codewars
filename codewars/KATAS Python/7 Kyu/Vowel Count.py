# This is the result of the "Vowel Count" 7 kyu exercise in Codewars, language used: Python
# Codewars

def get_count(sentence):
    vowel={'a','e','i','o','u'}
    count=0
    
    for letter in sentence:
        if letter in vowel:
            count+=1
        
    return count
