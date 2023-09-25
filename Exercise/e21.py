#printing sencond least score
if __name__ == '__main__':
    ml=[]
    for _ in range(int(input("size:"))):
        l1=[]
        name = input("name :")
        l1.append(name)
        score = float(input("score:"))
        l1.append(score)
        ml.append(l1)
    l1=[]
    for i in range(len(ml)):
        l1.append(ml[i][1])
    print(l1)
    a=min(l1)
    abc=[]
    for i in range((len(ml))):
        if(a==l1[i]):
            abc.append(ml[i])
    for i in range(len(abc)):
        ml.remove(abc[i])
    print(ml)
    l1=[]
    for i in range(len(ml)):
        l1.append(ml[i][1])
    b=min(l1)
    p=[]
    for i in range((len(ml))):
        if(b==l1[i]):
            p.append(ml[i][0])
    p.sort()
    for i in range(len(p)):
        print(p[i])