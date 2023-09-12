'''def rat(a):
    y=a("Enter name:")
    return y
m=rat(input)
#m=rat(print)
print(m)
'''
def rat(a):
    def han():
        print("a executing")
        a()
        print("a executed")
    return han

def abc():
    print("ABC value")
rathan=rat(abc)
rathan()