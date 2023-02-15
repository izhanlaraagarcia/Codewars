#This is the result of the "Counting Duplicates" 6 kyu exercise in Codewars, language used: Python
# Codewars

def duplicate_count(text):
    text_lower = text.lower()
    count = 0
    dic = {}
    
    for i in range(0,len(text_lower)):
        dic[text_lower[i]] = 0
        
    
    for key in dic:
        for i in range(0,len(text_lower)):
            if(key == text_lower[i]):
                dic[key] = dic[key] + 1
            
    for key in dic:
        if (dic[key] > 1):
            count = count + 1
    
    return count
