with open("sample_e48.txt") as a:
    re=a.read()
with open("sample_e48.txt","w") as a:
    b=re.replace("version","VER")
    a.write(b)
print(re,"\n--------------------")
print(b)
