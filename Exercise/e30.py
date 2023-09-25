from os import makedirs


a=[]
for i in range(6):
    marks=int(input(f"Enter the {i+1} student marks:"))
    a.append(marks)
a.sort()
print(a)