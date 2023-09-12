#args
def rat(a,*b):
    print(a)
    print(b)
rat(5,99,6,8,2,3)

#kwargs
def py(a,**b):
    print(a)
    print(b)
a=10
#for key,value in b.items():
b={"fruit1":"Apple","fruit2":"Banana","fruit3":"cherry"}
py(a,**b)