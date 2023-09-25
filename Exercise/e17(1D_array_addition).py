from array import *
size=int(input("Enter size of matrix:"))

a=array('i',[])
for i in range(size):
    aa=int(input("Enter the elements of first matrix:"))
    a.append(aa)

b=array('i',[])
for i in range(size):
    bb=int(input("Enter the elements of second matrix:"))
    b.append(bb)

c=array('i',[])
for i in range(size):
    c.append(a[i]+b[i])
print(c)