a=int(input("Enter the no. to find it is prime or not:"))
b=0
for i in range(2,a):
    if a%i==0:
        b=1
if (b==0 or a==1) and a!=0 :
    print(f"{a} is  prime")
elif b==1:
    print(f"{a} is NOT prime")
elif a==0:
    print(f"{a} is NOT prime nor composite")

