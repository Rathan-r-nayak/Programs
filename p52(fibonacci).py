def fibonacci(n):
        a=0
        b=1
        print(a,",",b,",")
        for i in range(n-2):
            temp=b
            b=b+a
            a=temp
            print(b,"\b,",end="")

a=int(input("Enter the no:"))
fibonacci(a)