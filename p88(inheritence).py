class A:
    def s1(self):
        print("s1 is printing")
    def s2(self):
        print("s2 is printing")
class B(A):
    def s3(self):
        print("s3 is printing")
    def s4(self):
        print("s4 is printing")
class C:
    def s5(self):
        print("s5 is printing")
    def s6(self):
        print("s6 is printing")
class D(B,C):
    def s7(self):
        print("s7 is printing")
    def s8(self):
        print("s8 is printing")
var1=A()
var2=B()
var3=C()
var4=D()
var1.s1()
var2.s1()