#cafe management system
# Define dictionaries for each category with their items and prices
coffees = {
    'espresso': 30,
    'latte': 40,
    'cappuccino': 45,
    'americano': 35,
    'mocha': 50,
    'flat white': 45
}

teas = {
    'black tea': 20,
    'green tea': 25,
    'chai': 30,
    'herbal tea': 35
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

juices = {
    'mango': 40,
    'banana': 30,
    'pine-apple': 25,
    'fruit-mix': 50,
    'apple': 40
}

# Combine all dictionaries into one main dictionary
menu = {
    'coffees': coffees,
    'teas': teas,
    'snacks': snacks,
    'juices': juices
}

# Function to display the cafe menu
def show_menu():
    print("\nCafe Menu:")
    for category, items in menu.items():
        print(f"\n{category.capitalize()}:")
        for item, price in items.items():
            print(f"  {item.capitalize()}: Rs. {price}")

# Function to handle ordering
def handle_order():
    order_items = {}
    while True:
        category = input("Enter the category you want to order from (e.g., 'coffees', 'teas', 'snacks', 'juices'): ").lower()
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