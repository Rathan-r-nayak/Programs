# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
s=set(map(int,input().split()))

op=int(input())
li=[]
for i in range(op):
    a=input()
    li=a.split()
    s1=set(map(int,input().split()))
    
    if(li[0]=="intersection_update"):
        s.intersection_update(s1)
    elif(li[0]=="update"):
        s.update(s1)
    elif(li[0]=="symmetric_difference_update"):
        s.symmetric_difference_update(s1)
    elif(li[0]=="difference_update"):
        s.difference_update(s1)
    li=[]
sum=0
for i in s:
    sum+=i
print(sum)




# TASK
# You are given a set and number of other sets. These number of sets have to perform some specific mutation operations on set

# .

# Your task is to execute those operations and print the sum of elements from set

# .

# Input Format

# The first line contains the number of elements in set
# .
# The second line contains the space separated list of elements in set .
# The third line contains integer , the number of other sets.
# The next lines are divided into parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.