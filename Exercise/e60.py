class Employee:
    company="Google"

    def __init__(self):
        self.name="Rathan"
        self.age=18
class Emp(Employee):
    pass

e1=Emp()
print(e1.name)