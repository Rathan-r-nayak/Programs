class CEO1:
    company="Google"
    def det(self):
        self.name="Sundar Pichai"
        self.age=49
        self.dob="10-06-1972"
class CEO2:
    company="Microsoft"
    def det(self):
        self.name="Satya Nadella"
        self.age=54
        self.dob="19-08-1967"
class CEO3(CEO1):
    company="Space-X"
    def det(self):
        super().det()
        return 
        self.name="Elon Musk"
        self.age=50
        self.dob="28-06-1971"
c1=CEO1()
c2=CEO2()
c3=CEO3()
c3.det()
print(c3.name)