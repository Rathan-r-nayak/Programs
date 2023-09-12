def dec(a):
    def han():
        print("a executing")
        a()
        print("a executed\n---------------------")
    return han
@dec
def name():
    print("name:Rathan")
@dec
def usn():
    print("Usn:4MW20CS062")
@dec
def age():
    print("age:18")


name()
usn()
age()