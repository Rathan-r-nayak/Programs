n=2
arr=[1]
res=n

for i in range(1,n-1):
    if i!=arr[i-1]:
        res=i
        break
print(res)