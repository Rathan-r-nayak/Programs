b=int(input("Enter the no."))
def factorial(a):
    if a==1:
        return 1
    else:
        i=1
        fac=1
        while(i<=a):
            fac=fac*(i)
            i+=1
    return fac
res=factorial(b)
print(res)