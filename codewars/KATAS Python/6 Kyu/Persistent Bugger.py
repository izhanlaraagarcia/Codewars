#CodeWars
def persistence(n):
    if n < 10:
        return 0
    nstr=str(n)
    t=1
    for i in nstr:
        t=t*int(i)
    return 1 + persistence(t)