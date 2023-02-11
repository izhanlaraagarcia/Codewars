#Codewars
# Hamming Distance Python
def hamming(a,b):
    distancia=0
    x=len(a)
    for i in range(x):
        if a[i] != b[i]:
        distancia+=1
    return distancia