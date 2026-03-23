pin = 1234

user_pin = int(input("Enter PIN: "))

if user_pin != pin:
    print("Wrong PIN")
    exit()

# Read balance
try:
    with open("balance.txt", "r") as f:
        balance = int(f.read())
except:
    balance = 0

while True:
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Show History")
    print("5. Exit")

    choice = input("Enter choice: ")

    # Deposit
    if choice == "1":
        amount = int(input("Enter amount: "))
        balance += amount
        print("Deposited successfully")

        with open("history.txt", "a") as f:
            f.write(f"Deposited: {amount}\n")

        with open("balance.txt", "w") as f:
            f.write(str(balance))

    # Withdraw
    elif choice == "2":
        amount = int(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdraw successful")

            with open("history.txt", "a") as f:
                f.write(f"Withdraw: {amount}\n")
        else:
            print("Insufficient balance")

        with open("balance.txt", "w") as f:
            f.write(str(balance))

    # Check Balance
    elif choice == "3":
        print("Current Balance:", balance)

    # Show History
    elif choice == "4":
        try:
            with open("history.txt", "r") as f:
                data = f.read()
                print("\n--- Transaction History ---")
                print(data)
        except:
            print("No history found")

    # Exit
    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Invalid choice")