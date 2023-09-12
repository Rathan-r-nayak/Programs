from stringprep import c22_specials


class computer:
    company="Lenovo"
    def __init__(self,ram,cost):
        self.ram=ram
        self.cost=cost

#Instamce Method     (this is also an Accessor)
    def spec(self):
        return self.ram

#mutators
    def set_cost(self,costwithgst):
        return self.cost+costwithgst

c1=computer("16GB",70000)
c2=computer("8GB",65000)
print(c1.cost)
print(c1.spec())
print(c1.set_cost(3500))
