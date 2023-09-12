class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,r):
        a=self.m1+r.m1    #78+95
        b=self.m2+r.m2    #89+85
        s3=student(a,b)
        return s3
    def __gt__(self,r):
        a=self.m1+self.m2
        b=r.m1+r.m2 
        csee= a if a>b else b
        return True if csee==a else False
s1=student(78,89)
s2=student(95,85)
s3=s1+s2
print(f"total in m1: {s3.m1}\ntotal in m2: {s3.m2}")
if s1>s2:
    print("s1 ha more avg")
else:
    print("s2 has more avg")