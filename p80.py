class terminal:
    def __init__(self,name,age,usn):
        print(self)
        self.name=name
        self.age=age
        self.usn=usn
    @classmethod
    def clcl(cls,string):
        var=string.split("-")
        print(cls)
        return cls(var[0],var[1],var[2])
'''a="rathan"
b=18
c="4MW20CS062"
p1=terminal(a,b,c)
#print(p1.name,p1.age,p1.usn)'''
p2=terminal.clcl("RATHAN-18-4MW20CS062")
print(p2.name)