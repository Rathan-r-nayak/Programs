a=44
def rat():
    def ttt():
        print(a)
        #global a
        #a=99
    a=55
    print("before calling ttt():",a)
    ttt()
    print("After calling ttt():",a)
rat()
print(a)