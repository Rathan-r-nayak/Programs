n=int(input("Enter the no. of elements:"))
a=list(map(int,input("Enter the numbers:").strip().split()))[:n]

for i in range(0,n-1):
    for j in range(i+1,n):
        if(a[i]==a[j]):
            for k in range(j,n-1):
                a[k]=a[k+1]
            n=n-1
            j=j-1

print(a)