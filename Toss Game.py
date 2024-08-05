#toss Program
import random
import sys

def end():
    sys.exit()

player = input("Enter Your Name: ").upper()

while True:
    playerchoice = input("Select Heads or Tails: ").lower()
    
    # Generate a random choice for the system (0 for Heads, 1 for Tails)
    syschoice = random.randint(0, 1)
    
    if syschoice == 0:
        print("Coin Turned up Heads")
    else:
        print("Coin Turned up Tails")
    
    if playerchoice == "heads":
        playerchoice = 0
    elif playerchoice == "tails":
        playerchoice = 1
    else:
        print("Invalid Input, Try again.")
        continue  # Retry the loop if input is invalid
    
    if playerchoice == syschoice:
        print(player, "You won!")
    else:
        print("You lost.")
    
    game = input("Do you want to play again? If yes, enter 'toss' or else enter 'end': ").lower()
    
    if game == "end":
        end()
    elif game != "toss":
        print("Invalid input. Exiting the game.")
        end()

