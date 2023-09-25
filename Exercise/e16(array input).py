from array import *
size=int(input("Enter the size of array"))
a=array('i',[])
for i in range(size):
    elem=int(input("Enter the elements of array"))
    a.append(elem)
print(a)
find=int(input("Enter the element to be find"))
for i in range(size):
    if a[i]==find:
        print(f"array found @ {i}")
print(a.index(find))