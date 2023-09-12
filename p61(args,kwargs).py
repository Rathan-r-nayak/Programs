def rat(b,*args,**kwargs):
    print("b",b)
    print("args",args[0])
    for key,value in kwargs.items():
        print(f"{key} is {value}")
a=["poco","redmi","realme","samsung"]
b=10
c={"fruit1":"Apple","fruit2":"Banana","fruit3":"cherry"}
rat(*a,b,**c)