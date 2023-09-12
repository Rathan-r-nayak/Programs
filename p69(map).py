def square(a):
   return a*a
def cube(b):
    return b**3
fn=[square,cube]
for i in range(10):
    ab=list(map(lambda x:x(i),fn))
    print(ab)