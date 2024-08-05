#Housie Game
import random
import time
import sys

def generate_ticket():
    return random.sample(range(1, 101), 10)

def draw_number(drawn_numbers):
    number = random.randint(1, 100)
    while number in drawn_numbers:
        number = random.randint(1, 100)
    drawn_numbers.add(number)
    return number

def check_winner(ticket):
    return len(ticket) == 0

def main():
    Names = []
    tickets = {}
    drawn_numbers = set()

    players = int(input("Enter number of players: "))
    
    if players < 2:
        print("This game needs at least two players.")
        sys.exit()
    
    for x in range(1, players + 1):
        name = input(f"Enter player {x} name: ").strip().lower()
        Names.append(name)
    
    for name in Names:
        tickets[name] = generate_ticket()
    
    print("\nGenerated Tickets:")
    for name, ticket in tickets.items():
        print(f"{name.capitalize()}'s ticket: {sorted(ticket)}")
    
    while True:
        number = draw_number(drawn_numbers)
        print(f"\nNumber drawn: {number}")
        time.sleep(1)

        for name, ticket in tickets.items():
            if number in ticket:
                ticket.remove(number)
                print(f"{name.capitalize()}'s ticket: {sorted(ticket)}")
                
                if check_winner(ticket):
                    print(f"{name.capitalize()} has won!")
                    print("\nGame Over")
                    print(f"Winner: {name.capitalize()}")
                    return

if __name__ == "__main__":
    main()
