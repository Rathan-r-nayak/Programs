#Faulty Calculator
op=input("Enter the operator")
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
if (((a==45)and(b==3)) or ((a==3)and(b==45))  and (op=='*') ):
    print("555")
    exit
elif (((a==56)and(b==9)) or ((a==9)and(b==56))  and (op=='+')):
    print("77")
    exit
elif (((a==56)and(b==6)) or ((a==6)and(b==56))  and (op=='/')):
    print("4")
    exit
elif op=='+':
    res=a+b
    print(res)
    exit
elif op=='-':
    res=a-b
    print(res)
    exit
elif op=='*':
    res=a*b
    print(res)
    exit
elif op=='/':
    if b==0:
        print("number 2 cannot be 0")
    else:
        res=a/b
        print(res)
    exit
