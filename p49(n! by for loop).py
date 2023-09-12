a=int(input("enter a no.:"))
def fac(a):
    faci=1
    for i in range(a):
        faci=faci*(i+1)
    return faci
res=fac(a)
print(res)