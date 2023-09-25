def sum(n):
    a=0
    for i in range(n+1):
        a=a+i
    return a
n=int(input("enter the no. to find the sum of natural no.:"))
res=sum(n)
print(res)