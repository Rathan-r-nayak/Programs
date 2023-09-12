n = int(input())
s = set(map(int, input().split()))
op=int(input())
li=[]

for i in range(op):
    a=input()
    li=a.split()
    
    if(li[0]=="pop"):
        s.pop()

    elif(li[0]=="remove"):
        s.remove(int(li[1]))
        
    elif(li[0]=="discard"):
        s.discard(int(li[1]))
    li=[]

sum=0
for i in s:
    sum+=i
print(sum)




# Task

# You have a non-empty set
# , and you have to execute commands given in

# lines.

# The commands will be pop, remove and discard.

# Input Format

# The first line contains integer
# , the number of elements in the set .
# The second line contains space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer , the number of commands.
# The next lines contains either pop, remove and/or discard commands followed by their associated value.