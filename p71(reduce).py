from functools import reduce
a=[5,6,1,52,5,88,2]
ab=reduce(lambda m,n:m+n, a)
print(ab)
