def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    split=int(n/k)
    i=0

    while i<split:
        p=list(string[3*i:3*i+3])
        for j in p:
            print(j,end="")
        print()
        i+=1

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)