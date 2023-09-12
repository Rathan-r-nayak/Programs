def add(a,b):
    return a+b
print("name=",__name__)
def strcat(st):
    return f"Hello {st}!"

if __name__=='__main__':
    a=5
    b=8
    st="Virat"
    sum=add(a,     b)
    greet=strcat(st)
    print(f"{greet}\nsum={sum}")
