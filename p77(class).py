class person:
    name=0
    age=0
    salary=0
    def ent_det(s):
        return f"name is {s.name},age is {s.age},& the salary is {s.salary}"

per_1=person()
per_2=person()
print("---------person1----------")
per_1.name=str(input("Enter the name  :"))
per_1.age=int(input("Enter the age   :"))
per_1.salary=float(input("Enter the salary:"))

print("---------person2----------")
per_2.name=str(input("Enter the name  :"))
per_2.age=int(input("Enter the age   :"))
per_2.salary=float(input("Enter the salary:"))

print("------------------------------------")
print("person 1=",per_1.ent_det())
print("person 2=",per_2.ent_det())
a=person()
print(a.name)