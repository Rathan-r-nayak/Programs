from cmath import sqrt


class Calculator:
    brand="CASIO"
    def __init__(self):
        pass
    def SQ(self,no):
        self.num=no
        return (self.num)**2
    
    def CUB(self,no):
        self.num=no
        return (self.num)**3
    
    def SQRT(self,no):
        self.num=no
        return sqrt(self.num)

print("1->square\n2->cube\n3->square root\n")
ch=int(input("Enter the choice:"))
n=int(input("Enter the number:"))
var1=Calculator()
if(ch==1):
    res=var1.SQ(n)
    print(f"square of {n} is {res}")
elif(ch==2):
    res=var1.CUB(n)
    print(f"cube of {n} is {res}")
elif(ch==3):
    res=var1.SQRT(n)
    print(f"square root of {n} is {res}")
else:
    print("Enter valid choice")