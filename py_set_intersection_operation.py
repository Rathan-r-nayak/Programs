# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=int(input())
s1 = set(map(int, input().split()))
n2=int(input())
s2 = set(map(int, input().split()))

s1=s1.intersection(s2)
print(s1)
print(len(s1))



# Task

# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

# Input Format

# The first line contains
# , the number of students who have subscribed to the English newspaper.
# The second line contains space separated roll numbers of those students.
# The third line contains , the number of students who have subscribed to the French newspaper.
# The fourth line contains space separated roll numbers of those students.