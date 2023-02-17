# This is the result of the "Multiples of 3 or 5" 6 kyu exercise in Codewars, language used: Python
# Codewars
def solution(number):
    list=[]
    
    for i in range(0, number):
        if (i%3==0 or i%5==0):
            list.append(i)
            
    return sum(list)
  
