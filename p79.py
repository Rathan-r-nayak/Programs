class ideal:
    logi=9
    #constructor
    def __init__(slff,aname,ausn,aage):
        slff.name=aname
        slff.usn=ausn
        slff.age=aage
    @classmethod
    def tech(cls,mp):
        cls.logi=mp

#s1=ideal()slff
#s2=ideal()
a=ideal("abc","062",18)
s2=ideal("Rathan","4MW20CS062",18)
s2.tech(100)
m=ideal(11,22,33)
print(m.logi)
print(s2.logi)
print(a.logi)
#print(m.logi)