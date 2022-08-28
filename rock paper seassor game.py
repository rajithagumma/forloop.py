print("GAME NAME IS ROCK PAPER SICCISSOR GAME")
name1=input("enter player1 name:")
name2=input("enter player2 name:")

print("now player1 turn to choose weapon number:")
print("1_rock")
print("2_paper")
print("3_seassor")
ch1=int(input("enter weapon number by player1:"))
while ch1<=3:
    if ch1==1:
        player1choice="rock"
        print("player1 choice is",player1choice)
        break
    elif ch1==2:
        player1choice="paper"
        print("player1 choice is",player1choice)
        break
    else:
        player1choice="seassor"
        print("player1 choice is",player1choice)
        break
ch2=int(input("enter weapon  number by player2:"))
while ch2<=3:
    if ch2==1:
        player2choice="rock"
        print("player2 choice is",player2choice)
        break
    elif ch2==2:
        player2choice="paper"
        print("player2 choice is",player2choice)
        break
    else:
        player2choice="seassor"
        print("player2 choice is",player2choice)
        break
if (player1choice=="rock") and (player2choice=="paper"):
    print("congraslations player2",name2,"you are the winner")
    print("player1",name1,"is a runner")
elif (player1choice=="paper") and (player2choice=="seasor"):
     print("congraslations player2",name2,"you are the winner")
     print("player1",name1,"is a runner")
elif (player1choice=="seasosr") and (player2choice=="rock"):
     print("congraslations player2",name2,"you are the winner")
     print("player1",name1,"is a runner")
elif (player1choice=="paper") and (player2choice=="rock"):
    print("congraslations player1",name1,"you are the winner")
    print("player2",name2,"is a runner")
elif (player1choice=="seassor") and (player2choice=="paper"):
     print("congraslations player1",name1,"you are the winner")
     print("player2",name2,"is a runner")
elif (player1choice=="rock") and (player2choice=="seassor"):
     print("congraslations player1",name1,"you are the winner")
     print("player2",name2,"is a runner")

else:
    print("no one")