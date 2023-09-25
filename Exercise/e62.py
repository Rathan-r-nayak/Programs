class c1:
    c=1
    def user(self):
        self.name="rathan"
class c2(c1):
    c=2
    def user(self):
        self.name="RATHAN"
class c3(c2):
    c=3
    def user(self):
        self.name="RATHAN R NAYAK"
p1=c3()
print(p1.c)
p1.user()
print(p1.name)