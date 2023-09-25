import random
i=0
j=0
k=0
a=[]
set0=[]
set1=[]
set2=[]
set3=[]
set4=[]
for rat in range(5):
    elem1=random.randrange(0,2)
    set0.append(elem1)

for rat in range(5):
    elem1=random.randrange(0,2)
    set1.append(elem1)

for rat in range(5):
    elem1=random.randrange(0,2)
    set2.append(elem1)

for rat in range(5):
    elem1=random.randrange(0,2)
    set3.append(elem1)

for rat in range(5):
    elem1=random.randrange(0,2)
    set4.append(elem1)

print("---------------------")
mainset=[set0,set1,set2,set3,set4]
for k in range(len(mainset)):
    print("|",mainset[k],"|")

#while x in 