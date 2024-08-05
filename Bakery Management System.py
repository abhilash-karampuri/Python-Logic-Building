# Define dictionaries for each category with their items and prices
cakes = {
    'pine-apple': 250,
    'chocolate': 450,
    'butterscotch': 300,
    'black forest': 500
}

snacks = {
    'burger': 200,
    'pizza': 300,
    'momos': 400,
    'veg nuggets': 200,
    'chicken nuggets': 250,
    'muffins': 100,
    'bagels': 50
}

decoration_items = {
    'color-ribbons': 100,
    'balloons': 50,
    'candles': 20,
    'blast': 200,
    'smoke-spray': 250
}

coffee = {
    'espresso': 30,
    'latte': 40,
    'cappuccino': 45,
    'americano': 35,
    'mocha': 50,
    'flat white': 45
}

juices = {
    'mango': 40,
    'banana': 30,
    'pine-apple': 25,
    'fruit-mix': 50,
    'apple': 40
}

shakes = {
    'mango': 140,
    'banana': 130,
    'badam': 160,
    'chocolate': 180,
    'oreo': 60
}

ice_creams = {
    'vanilla': 100,
    'chocolate': 200,
    'strawberry': 150,
    'butterscotch': 200,
    'pista': 140
}

# Combine all dictionaries into one main dictionary
menu = {
    'cakes': cakes,
    'snacks': snacks,
    'decoration items': decoration_items,
    'coffee': coffee,
    'juices': juices,
    'shakes': shakes,
    'ice creams': ice_creams
}

# Function to display the bakery menu
def show_menu():
    print("\nBakery Menu:")
    for category, items in menu.items():
        print(f"\n{category.capitalize()}:")
        for item, price in items.items():
            print(f"  {item.capitalize()}: Rs. {price}")

# Function to handle ordering
def handle_order():
    order_items = {}
    while True:
        category = input("Enter the category you want to order from (e.g., 'cakes', 'snacks', 'coffee', etc.): ").lower()
        if category in menu:
            print(f"\nSelect from {category}:")
            for item, price in menu[category].items():
                print(f"  {item.capitalize()}: Rs. {price}")
                
            while True:
                item = input("Enter the item you want to order (or type 'done' to finish): ").lower()
                if item == 'done':
                    break
                if item in menu[category]:
                    quantity = int(input(f"Enter the quantity for {item.capitalize()}: "))
                    if quantity > 0:
                        if item in order_items:
                            order_items[item][1] += quantity
                        else:
                            order_items[item] = (menu[category][item], quantity)
                    else:
                        print("Quantity should be a positive number.")
                else:
                    print("Item not found in the selected category.")
        else:
            print("Invalid category. Please choose a valid category.")
        
        more_orders = input("Do you want to order from another category? (yes/no): ").lower()
        if more_orders != 'yes':
            break
    
    return order_items

def calculate_total(order_items):
    total = 0
    for item, (price, quantity) in order_items.items():
        total += price * quantity
    return total

def main():
    show_menu()  # Show the menu first
    
    order_items = handle_order()  # Take the order
    
    if order_items:
        print("\nYour Order:")
        for item, (price, quantity) in order_items.items():
            print(f"  {item.capitalize()}: Rs. {price} x {quantity} = Rs. {price * quantity}")
        
        total = calculate_total(order_items)
        print(f"\nTotal Bill: Rs. {total}")
        
    else:
        print("No items ordered.")

if __name__ == "__main__":
    main()
