def deposit(balance):
    amount = int(input("Enter Amount for Deposit: "))
    balance += amount
    return balance

def withdraw(balance):
    amount = int(input("Enter Withdraw Amount: "))
    if amount <= balance:
        balance -= amount
        print(f"Amount withdrawn: {amount}. Remaining Balance: {balance}")
    else:
        print("Insufficient Balance")
    return balance

def showBalance(balance):
    print(f"Balance Amount: {balance}")

def main():
    balance = 0
    while True:
        choice = input("Enter operation (Deposit / Balance Enquiry / Withdraw / Exit): ").lower()
        
        if choice == "deposit":
            balance = deposit(balance)
        elif choice == "balance enquiry":
            showBalance(balance)
        elif choice == "withdraw":
            balance = withdraw(balance)
        elif choice == "exit":
            print("Thankyou")
            break
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
