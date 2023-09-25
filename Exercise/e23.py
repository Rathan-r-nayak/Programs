if __name__ == '__main__':
    n = int(input("size"))
    student_marks = {}
    for _ in range(n):
        name, *line = input("name m1 m2 m3:").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(name,"=",scores,student_marks)

    a=0
    for i in student_marks[query_name]:
        a=a+i
    print('{0:.2f}'.format(a/3))