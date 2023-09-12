def rat(x,y):   #fn. defn. 
    """this is a rat() function which add 2 values"""
    print("This is \'rat()\' Function")
    z=x+y
    return z

a=int(input("Enter a no."))
b=int(input("Enter another no."))
c=rat(a,b)   #fn. call
print(c,"\n-----------------")
print(rat.__doc__ )