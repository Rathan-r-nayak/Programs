'''class info:
    name=0
    salary=0
    company=0'''
class person:
    name=0
    age=0
    salary=0

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

print("---------person1----------")
print(per_1.name)
print(per_1.age)
print(per_1.salary)
print("---------person2----------")
print(per_2.name)
print(per_2.age)
print(per_2.salary)
