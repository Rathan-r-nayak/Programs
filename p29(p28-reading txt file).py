a=open("p28(text file).txt","rt")
c=a.readline()          # prints only 4 letters of line1
print(c)
b=a.readline()       # prints rest of letters of line1
print("rat:",b)

print(a.readline())  # prints line2 
 
"""for line in a:
    print("\n\n",line,"\n\n")"""
a.close()