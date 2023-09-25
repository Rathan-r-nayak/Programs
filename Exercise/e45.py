def game(hs):
    with open("game_e45.txt") as a:
        re=a.read()
    if (hs>int(re)):
        with open("game_e45.txt","w") as a:
            a.write(str(hs))

hs=int(input("Enter the score:"))
game(hs)