age=int(input("enter your age:"))
if (age<18 and age>7):
    print("you cant drive a vehicle because you are too young to drive")
elif age==18:
    print("your age is 18 but we can't decide come to RTO for further information")
elif(age>18 and age<=100):
    print("you can drive")
else:
    print("you are unfit to drive vehicle")