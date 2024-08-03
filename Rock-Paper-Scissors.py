'''Write a program for stone paper scissors.
The computer generated any random choice from stone paper scissors and user need to enter the value.
And this play should continue for n times. After n times score is calculated and winner is displayed'''
import random
n=int(input())

game=["rock","paper","scissors"]
#rock=0  ,  paper=1,   scissors=2
system=random.randint(0,2)
systeminput=game[system]
#print("System Choosen:",systeminput)
for x in range(n):
    user=int(input("Enter 0 for rock, 1 for paper, 2 for scissors"))
    userinput=game[user]
    print("User Choosen:",userinput)
    scoresys=0
    scoreuser=0
    if((system==0 and user==0) or (system==1 and user==1) or (system==2 and user==2)):
        scoresys=0
        scoreuser=0
        print("Tie")
    elif ((system==0 and user==1) or (system==1 and user==2) or (system==2 and user==0)):
        scoreuser+=1
        print("User you win")
    else:
        scoresys+=1
        print("System wins")
print("Score of System:",scoresys)
print("Score of User:",scoreuser)
if scoresys>scoreuser:
    print("System won the Game")
elif scoresys<scoreuser:
    print("You won the Game")
else:
    print("Tie")
'''1. rock x rock = tie  0 and 0 = print scoreofsystem=0 scoreuser=0
2.rock x paper= paper -- user win
3. rock x scissors= rock ----system win
4. paper x rock = paper---system win
5. paper x paper =tie
6. paperx scissors = scissors----user win
7. scissors x rock = rock ---user win
8. scissors x paper = scissors----system
9. scissors x scissors = tie'''
