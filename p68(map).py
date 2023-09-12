'''
a=[5,6,1,52,5,88,2]
a[6]=a[5]+a[6]
print("before map fn.",a)
a=list(map(str,a))
a[6]=a[5]+a[6]
print("after map fn. ",a)
'''
rat=[2,6,23,55,5,12,3]
#def square(a):
#    return a*a
#las=list(map(square,rat))
las=list(map(lambda a:a*a,rat))
print(las)