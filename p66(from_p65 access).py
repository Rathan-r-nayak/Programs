import p65
n1=int(input("Enter a no."))
n2=int(input("Enter another no."))
res=p65.add(n1,n2)
strs=str(input("Enter your name"))
strr=p65.strcat(strs)
print(f"{strr}\nsum is {res}")
