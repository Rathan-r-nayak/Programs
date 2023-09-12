class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(s11,s22):
        a=s11.m1+s11.m2
        b=s22.m1+s22.m2
        s3=student(a,b)
        return s3
    def __str__(self):
        return self.m1,self.m2
s1=student(55,96)
s2=student(85,75)
s3=s1+s2
print(s3.__str__())