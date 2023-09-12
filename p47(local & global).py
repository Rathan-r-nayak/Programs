def clcl():
        a=100
        return(a)
def rat():
    global a
    a=55
    print("a=",a)
    a=clcl()
    print("a=",a)
rat()
print(a)