with open("sample_e47.txt") as a:
    re=a.read()
re=re.replace("donkey","#####")
with open("sample_e47.txt","w") as a:
    a.write(re)
