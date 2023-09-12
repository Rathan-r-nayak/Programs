#Astrolonger's stars 

n=int(input("Enter the no. of rows"))
bolea=int(input("Enter 1(true) or 0(false)"))
#bolea=bool(bole)
try:
    i=1
    if (bolea==1):
        while i<=n:
            print("*"*i)
            i+=1
    elif (bolea==0):
        i=1
        while i<=n:
            print("*"*(n+1-i))
            i+=1
    #else:
        #None
except Exception as error:
    print("error")