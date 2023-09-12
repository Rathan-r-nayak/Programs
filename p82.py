class name:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def compare(self,p2):
        if (self.age==p2.age):
            return True 
        else:
             return False 
p1=name("Rathan",18)
p2=name("ttt",22)
p2.age=18
print(p1.compare(p2))
#print(p1.age==p2.age)