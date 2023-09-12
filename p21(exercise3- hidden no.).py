#Guess the number before 9 chances
a=11
i=1
print("you have 9 chances to guess no.")
while i<=9:
    b=int(input("Enter the no."))
    print("no. of chances left:",(9-i))
    if b<a:
        print("Entered no. is Less than hidden no.")
    elif b==a:
        print("Entered no. is correct")
        print("you completed within",i,"chances")
        exit()
    else:
        print("Entered no. is greater than hidden no.")
    i=i+1
if i==10:
    print("Game Over")