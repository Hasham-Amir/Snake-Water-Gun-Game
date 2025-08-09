import random,os
def game():
    print("Enter 111 to exit")
    playerPoints=0
    computerPoints=0
    tries=0

    reversedict={1:"Snake", 0:"Water", -1:"Gun"}
    while True:
        computer=random.choice([-1,0,1])
        print("-1,0,1")
        try:
            player=int(input("Pick a number from the list"))
            if player==111:
                break
            if player not in reversedict:
                print("Invalid Choice please pick -1,0 or 1.")
                continue
        except ValueError:
            print("Enter a valid number")
            continue

        print(f'you chose {reversedict[player]} and Computer chose {reversedict[computer]}')

        if computer==player:
            print("Draw")
        else:
            if ((computer==1 and player==-1) or (computer==0 and player==1) or (computer==-1 and player==0)):
                print("You won")
                playerPoints+=1

            else:
                print("you lose")
                computerPoints+=1
        tries+=1

    print(f'Computer won {computerPoints} times\nYour won {playerPoints} times')
    
    percentage= (playerPoints*100)//tries

    with open("highWinPercentage.txt") as f:
        highpercent=f.read()
        if (highpercent!=""):
            highpercent=int(highpercent)
        else:
            highpercent=0
    
    if percentage>highpercent:
        #write this percentage to file
        with open("highWinPercentage.txt","w") as f:
            f.write(f"Highest Win Percentage is {str(percentage)}%")
    return percentage

game()