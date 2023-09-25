if __name__ == '__main__':
    ml=[]
    for _ in range(int(input("students (N):"))):
        l1=[]
        name = input("name :")
        l1.append(name)
        score = float(input("grade:"))
        l1.append(score)
        ml.append(l1)
    l1=[]
    a=min()
    for i in range(len(ml)):
