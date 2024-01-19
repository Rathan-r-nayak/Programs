A=[16,17,4,3,5,2]
N=6


li=[]
# l=A[0]
if(A[0]>A[1]):
    li.append(A[0])
for i in range(1,N-1):
    if(A[i-1]<A[i] and A[i+1]<A[i]):
        li.append(A[i])
li.append(A[-1])

l=0
for i in range(1,len(li)):
    if(li[l]<li[i]):
        l=i

print(li[l:])