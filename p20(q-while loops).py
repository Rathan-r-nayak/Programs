"""a=int(input("enter no."))
while a<100:
    a=int(input("enter no."))"""
while (True):
    a=int(input("enter a number:"))
    if a>100:
        print("no. is greater than 100")
        break
    else:
        print("no. is not greater than 100")
        continue