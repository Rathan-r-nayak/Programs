class ideal:
    #constructor
#     self=s2   aname="Rathan" ausn="4MW20CS062"   aage=18
    def __init__(self,aname,ausn,aage):
        self.name=aname
        self.usn=ausn
        self.age=aage
#s1=ideal()
#s2=ideal()
s2=ideal("Rathan","4MW20CS062",18)
print(s2.name)
print(s2.usn)
print(s2.age)