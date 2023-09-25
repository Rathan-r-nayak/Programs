class Programmer:
    company="Microsoft"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def ptdetail(self):
        print(f"employee name is {self.name} and age is {self.age} having {self.salary} salary\\month\n@ {Programmer.company}")

emp1=Programmer("Rathan",18,500000)
emp2=Programmer("logi",27,100000)
emp1.ptdetail()
emp2.ptdetail()