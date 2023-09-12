import random
r=random.randint(5,11)
b=random.randrange(0,2)
d=random.random()#*100
c=random.random()*100
#a=["poco","redmi","realme","samsung"]
a=random.choice(["poco","redmi","realme","samsung"])
print("random.randint:",r)
print("random.randrange",b)
print("random.random",c)
print("random.choice",a)