def isfn(a):
    return("is "+a)


a=str(input("Enter string"))
if a.startswith("is"):
    print(a)
else:
    c=isfn(a)
    print(c)