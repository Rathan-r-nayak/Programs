if __name__ == '__main__':
    n = int(input("size:"))
    print("ELEM:")
    arr = map(int, input().split())
    l1=[]
    for i in arr:
        l1.append(i)
    print(l1)
    l1=set(l1)
    l1=list(l1)
    l1.sort()
    print(l1)
    print(len(l1)-2)
    print(l1[len(l1)-2])