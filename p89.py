class A:
    def __init__(self):
        print("---INIT of A---")
    def rathan(self):
        print("RATHAN FUNCTION EXECUTING")
class B:
    def __init__(self):
        print("---INIT of B---")
class C(A,B):
    def __init__(self):
        print("---init of C---")
        super().__init__()
        super().rathan()

a=C()