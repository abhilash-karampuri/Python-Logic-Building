import random
import time

# Define snakes and ladders
snakes = {
    18: 6,
    29: 7,
    61: 16,
    96: 76,
    72: 47
}
ladders = {
    2: 37,
    16: 54,
    15: 82,
    9: 14,
    50: 91,
    74: 87
}

def apply_snakes_and_ladders(position):
    if position in snakes:
        return snakes[position]
    if position in ladders:
        return ladders[position]
    return position

def take_turn(player):
    while True:
        roll = random.randint(1, 6)
        player += roll
        if player > 100:
            player = 100  # Prevent going past 100
        player = apply_snakes_and_ladders(player)
        print(f"Player rolled a {roll}. Player is at {player}")
        time.sleep(1)
        if roll != 6:
            break  # End the turn if roll is not 6
    return player

# Initialize player positions
p1 = 0
p2 = 0

# Game loop
while p1 < 100 and p2 < 100:
    print("\nP1's turn:")
    p1 = take_turn(p1)
    if p1 == 100:
        print("P1 is the winner!")
        break
    
    print("\nP2's turn:")
    p2 = take_turn(p2)
    if p2 == 100:
        print("P2 is the winner!")
        break

print("Game Over!")
