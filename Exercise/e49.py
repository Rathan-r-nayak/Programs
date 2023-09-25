with open("sample_e49.txt") as a:
    re=a.read().lower()
l1=["exercise","desktop","oneDrive","python"]
i=0
while i<len(l1):
    b=re.replace(l1[i],"**********")
    with open("sample_e49.txt","w") as f:
        f.write(b)
    b=0
    i=+1
