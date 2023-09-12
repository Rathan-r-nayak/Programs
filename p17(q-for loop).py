a=["rathan",9,55,1,32,3,41,22,5,6,"5"]
for i in a:
    if str(i).isnumeric():
        if i<6:
            print(i,"is less than 6")
        else:
            print(i,"is greater than 6")