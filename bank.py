import os
from datetime import datetime

# ---------- VTU BANK LOGO ----------

def show_logo():
    print("\n====================================")
    print("           🏦 VTU BANK")
    print("====================================\n")

# ---------- BALANCE FUNCTIONS ----------

def get_balance():
    if not os.path.exists("balance.txt"):
        return 0
    with open("balance.txt", "r") as f:
        data = f.read().strip()
        return int(data) if data else 0

def set_balance(balance):
    with open("balance.txt", "w") as f:
        f.write(str(balance))

# ---------- HISTORY FUNCTIONS ----------

def add_history(action, amount, balance):
    time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
    with open("history.txt", "a") as f:
        f.write(f"{time}|{action}|{amount}|{balance}\n")

def show_history():
    try:
        with open("history.txt", "r") as f:
            lines = f.readlines()

            if not lines:
                print("📭 No transactions yet")
                return

            print("\n====== TRANSACTION HISTORY ======\n")

            for i, line in enumerate(lines, start=1):
                parts = line.strip().split("|")

                if len(parts) == 4:
                    time, action, amount, balance = parts
                    print(f"[{i}] {time} | {action:<8} | ₹{amount} | Bal: ₹{balance}")

            print("\n================================")

    except FileNotFoundError:
        print("📭 No history found")

# ---------- BANK OPERATIONS ----------

def deposit(amount):
    if amount <= 0:
        print("❌ Enter a valid positive amount!")
        return

    balance = get_balance()
    balance += amount
    set_balance(balance)

    add_history("Deposit", amount, balance)
    print("✅ Deposit successful!")

def withdraw(amount):
    if amount <= 0:
        print("❌ Enter a valid positive amount!")
        return

    balance = get_balance()

    if amount > balance:
        print("❌ Insufficient balance!")
        return

    balance -= amount
    set_balance(balance)

    add_history("Withdraw", amount, balance)
    print("✅ Withdrawal successful!")

# ---------- MAIN MENU ----------

while True:
    show_logo()

    print("====== BANK MENU ======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Show History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            amount = int(input("Enter amount: "))
            if amount <= 0:
                print("❌ Amount must be greater than 0")
                continue
            deposit(amount)
        except ValueError:
            print("❌ Enter a valid number!")

    elif choice == "2":
        try:
            amount = int(input("Enter amount: "))
            if amount <= 0:
                print("❌ Amount must be greater than 0")
                continue
            withdraw(amount)
        except ValueError:
            print("❌ Enter a valid number!")

    elif choice == "3":
        print(f"💰 Current Balance: ₹{get_balance()}")

    elif choice == "4":
        show_history()

    elif choice == "5":
        print("🙏 Thank you for using VTU BANK!")
        break

    else:
        print("⚠️ Invalid choice")