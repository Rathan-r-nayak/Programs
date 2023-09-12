a={1,2}
b={3,4}
#b=set([1,5,1.5,55,525])
#c=([5,8,65])
c=set()
d={5,9,8}
print("a=",a)
print("type of a=",type(a))
print("b=",b)
print("type of b=",type(b))
print("c=",c)
print("type of c=",type(c))
print("d=",d)
print("type of d=",type(d))

print("----------------------------------------------")
print("----------------------------------------------")

print("d before adding 15,2     =",d)
d.add(15)
d.add(2)
print("d  after adding 15,2+    =",d)
print("union (1,2,5)            =",d.union({1,2,5}))
print("d                        =",d)
print("intersection (1,2,5)     =",d.intersection({1,2,5}))
print("d                        =",d)
print("min. value in d          =",min(d))
print("max. value in d          =",max(d))
print(b.isdisjoint(a))
