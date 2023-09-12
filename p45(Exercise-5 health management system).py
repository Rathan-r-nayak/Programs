# Health Management System
from os import write


def getdate():
    import datetime
    return datetime.datetime.now()

name=int(input("Press:  1-Harry  2-Rohan  3-Hammad:\n"))
typ=int(input("Press:   1-Exercise    2-Diet:\n"))
lorre=int(input("1-log 2-retriew"))
#----------------------------------------------------------------
date=getdate()
if (typ==1):
    a=str(input("Enter what you done in gym ?:\n"))
elif (typ==2):
    a=str(input("Enter what you eated ?:\n"))
else:
    print("Pls enter valid option")
    exit()
ray=str(date)+"  -"+str(a)
#----------------------------------------------------------------
if (typ==1):
    if (name==1):
        date=getdate()
        f=open("p39(Harry-exercise).txt","+r")
        f.write(str(date))
        f.write(a)
        print("Succesively Writtened")
        #if lorre==2:
            #print(f.readline())
        f.close()
    elif (name==2):
        date=getdate()
        f=open("p41(Rohan-exercise).txt","+r")
        f.write(str(date))
        f.write(a)
        print("Succesively Writtened")
        #if lorre==2:
            #print(f.read())
        f.close()
    elif (name==3):
        date=getdate()
        f=open("p43(Hammad-exercise).txt","+r")
        f.write(str(date))
        f.write(a)
        print("Succesively Writtened")
        #if lorre==2:
            #print(f.read())
        f.close()
    else:
        print("pls check name option")
        exit()

elif (typ==2):
    if (name==1):
        #date=getdate()
        f=open("p40(Harry-diet).txt","+r")
        #f.write(date)
        f.write(ray)
        print("Succesively Writtened")
        #if lorre==2:
            #print(f.read())
        f.close()
    elif (name==2):
        date=getdate()
        cc=input("What you eated")
        f=open("p42(Rohan-diet).txt","+r")
        f.write(str(date))
        f.write(cc)
        print("Succesively Writtened")
        #if lorre==2:
            #print(f.read())
            #print(rat)
        f.close()
    elif (name==3):
        date=getdate()
        f=open("p44(Hammad-diet).txt","+r")
        f>write(str(date))
        f.write(a)
        print("Succesively Writtened")
        #if lorre==2:
            #print(f.read())
        f.close()
    else:
        print("pls check name option")
else:
    print("Pls check")
    exit()


if lorre==2:
    if (typ==1):
        if (name==1):
            f=open("p39(Harry-exercise).txt","+r")
            print(f.read())
        elif (name==2):
            f=open("p41(Rohan-exercise).txt","+r")
            print(f.read())
        elif (name==3):
            f=open("p43(Hammad-exercise).txt","+r")
            print(f.read())
elif (typ==2):
    if (name==1):
        f=open("p40(Harry-diet).txt","+r")
        print(f.read())
        f.close()
    elif (name==2):
        f=open("p42(Rohan-diet).txt","+r")
        print(f.read(cc))
        f.close()
    elif (name==3):
        print(f.read())
        f.close()