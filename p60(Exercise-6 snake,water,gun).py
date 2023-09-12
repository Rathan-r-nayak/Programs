from random import randint
print("-----------------------------------------------")
print("points for win=1\npoints for draw=0.5\npoints for loose=0")
i=0
hmn=0
cmp=0
#c_choice=[1,2,3]
while i<10:
    print("----------------------------------------------------------------")
    choice=0
    choice=int(input("Enter ur choice \n---1-snake  2-water  3-gun---::"))
    import random
    #d_choice=["snake","water","gun"]
    #rat=random.choice(d_choice)
    #c_choice=[1,2,3]
    c_choice=random.randint(1,3)
    #choosenc=random.randint(0,3)
    if (choice==c_choice):
        print("Match Draw")
        cmp+=1
        hmn+=1
    else:
        if ((choice==1) and (c_choice==2)):
            print("You Won")
            hmn+=1
        elif ((choice==1) and (c_choice==3)):
            print("Opponent Won")
            cmp+=1
        elif ((choice==2) and (c_choice==1)):
            print("Opponent Won")
            cmp+=1
        elif ((choice==2) and (c_choice==3)):
            print("You Won")
            hmn+=1
        elif ((choice==3) and (c_choice==1)):
            print("You Won")
            hmn+=1
        elif ((choice==3) and (c_choice==2)):
            print("Opponent Won")
            cmp+=1
        else:
            print("Invalid i/p")
    i+=1
print(f"-------------------------------\nScore card in 10 matches\nYOU      :{hmn}\nOPPONENT:{cmp}\n-------------------------------\n")
if(hmn>cmp):
    print("YOU WON THE 10 MATCH TOURNAMENT")
elif(hmn==cmp):
    print("TOURNAMENT TIED")
else:
    print("OPPONENT WON THE 10 MATCH TOURNAMENT")
#c_choice=["1-snake","2-water","3-gun"]