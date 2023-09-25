class A:
    company="Google"
class B:
    company="Microsoft"
class c(A,B):
    pass
p=c()
print(p.company)