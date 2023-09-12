class student:
    def __init__(self,mk1,mk2):
        self.m1=mk1
        self.m2=mk2
    def __mul__(self,o2):
        a=self.m1*o2.m1
        b=self.m2*o2.m2
        s3=student(a,b)
        return s3
    def __lt__(self,s22):
        aa=self.m1+self.m2
        bb=s22.m1+s22.m2
        cc=aa<bb
        return True if cc==True else False

s1=student(88,56)
s2=student(90,46)
s3=s1*s2
print(s3.m2)
if s1<s2:
    print("sum of s1 is smaller")
else:
    print("sum of s2 is smaller")
