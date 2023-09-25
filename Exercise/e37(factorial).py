def fac(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return n*fac(n-1)


n=int(input("enter the no. to find factorial:"))
res=fac(n)
print(f"factorial of {n} is {res}")