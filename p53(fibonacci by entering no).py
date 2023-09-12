#0,1,1,2,3,5,8,13,21,34,......
def fibonacci(n):
    a=0
    b=1
    rat=0
    
    if n==1:
        print(a)
    elif n==2:
        print(b)
    else:
    #print(a,",",b,",")
        for i in range(n-2):
            a,b=b,(b+a)
            #temp=b
            #b=b+a
            #a=temp
            #rat=rat+1
        print(b)
a=int(input("Enter the no."))
fibonacci(a)