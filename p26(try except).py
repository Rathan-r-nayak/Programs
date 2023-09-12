a=input("Enter no.:")
b=input("Enter another no.:")
try:
    print("sum is:",int(a)+int(b))
except Exception as error:
    print(error)
    #None
print("concatination is:",a+b)


"""
a=(5,9,3,44)
try:
    a.append(55)
except Exception as error:
    print(error)
print(a)
"""