with open("sample_e50.txt") as f: 
    a=f.read()
l1=["Rathan","3","4MW20CS062","11-02-2022","SMVITM",]
a1=a.replace("<NAME>",l1[0])
a2=a.replace("<CLASS>",l1[1])
a3=a.replace("<USN>",l1[2])
a4=a.replace("<C_ADRESS>",l1[3])
a5=a.replace("<DATE>",l1[4])

with open("sample_e50.txt","w") as f:
    f.write(a1+a2+a3+a4+a5)
