from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os

# ------------------ FILE ------------------
DATA_FILE = "bank_data.json"

# ------------------ LOAD DATA ------------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

users = load_data()
current_user = None

# ------------------ LOGIN ------------------

def login():
    global current_user

    username = user_entry.get()
    password = pass_entry.get()

    if username in users:
        if users[username]["password"] == password:
            current_user = username
            login_window.destroy()
            open_bank()
        else:
            messagebox.showerror("Error", "Wrong password")
    else:
        # create new user
        users[username] = {
            "password": password,
            "balance": 0,
            "history": []
        }
        save_data(users)
        current_user = username
        messagebox.showinfo("Success", "Account created!")
        login_window.destroy()
        open_bank()


# ------------------ BANK FUNCTIONS ------------------

def deposit():
    try:
        amount = int(entry.get())
        if amount <= 0:
            raise ValueError

        users[current_user]["balance"] += amount
        users[current_user]["history"].append(f"+ ₹{amount}")
        save_data(users)

        result_label.config(text=f"Deposited ₹{amount}")
        update_balance()

    except:
        messagebox.showerror("Error", "Enter valid amount")


def withdraw():
    try:
        amount = int(entry.get())

        if amount > users[current_user]["balance"]:
            result_label.config(text="Insufficient Balance")
        else:
            users[current_user]["balance"] -= amount
            users[current_user]["history"].append(f"- ₹{amount}")
            save_data(users)

            result_label.config(text=f"Withdrawn ₹{amount}")
            update_balance()

    except:
        messagebox.showerror("Error", "Enter valid amount")


def update_balance():
    bal = users[current_user]["balance"]
    balance_label.config(text=f"₹ {bal}")


def show_history():
    hist = users[current_user]["history"]
    if not hist:
        result_label.config(text="No transactions")
    else:
        result_label.config(text="\n".join(hist[-5:]))

# ------------------ BANK UI ------------------

def open_bank():
    global entry, result_label, balance_label

    root = Tk()
    root.title("VTU BANK")
    root.geometry("400x600")
    root.configure(bg="#0f172a")

    # Logo
    try:
        img = Image.open("logo.png").resize((120, 120))
        logo = ImageTk.PhotoImage(img)
        Label(root, image=logo, bg="#0f172a").pack(pady=10)
        root.logo = logo
    except:
        pass

    Label(root, text=f"Welcome {current_user}",
          fg="white", bg="#0f172a",
          font=("Arial", 16)).pack()

    # Balance Card
    frame = Frame(root, bg="#1e293b", padx=20, pady=20)
    frame.pack(pady=15, padx=20, fill="x")

    Label(frame, text="Current Balance",
          fg="lightgray", bg="#1e293b").pack()

    balance_label = Label(frame, text="₹ 0",
                          fg="#22c55e", bg="#1e293b",
                          font=("Arial", 24, "bold"))
    balance_label.pack()

    update_balance()

    entry = Entry(root, font=("Arial", 14), justify="center")
    entry.pack(pady=15, ipadx=10, ipady=5)

    def btn(text, cmd):
        return Button(root, text=text, command=cmd,
                      bg="#22c55e", fg="black",
                      width=20)

    btn("Deposit", deposit).pack(pady=5)
    btn("Withdraw", withdraw).pack(pady=5)
    btn("Check Balance", update_balance).pack(pady=5)
    btn("History", show_history).pack(pady=5)

    Button(root, text="Exit", command=root.quit,
           bg="red", fg="white").pack(pady=10)

    result_label = Label(root, text="", fg="white", bg="#0f172a")
    result_label.pack(pady=10)

    root.mainloop()

# ------------------ LOGIN UI ------------------

login_window = Tk()
login_window.title("VTU BANK LOGIN")
login_window.geometry("300x300")
login_window.configure(bg="#0f172a")

Label(login_window, text="VTU BANK",
      fg="white", bg="#0f172a",
      font=("Arial", 18, "bold")).pack(pady=20)

user_entry = Entry(login_window)
user_entry.pack(pady=10)

pass_entry = Entry(login_window, show="*")
pass_entry.pack(pady=10)

Button(login_window, text="Login",
       command=login, bg="#22c55e").pack(pady=20)

login_window.mainloop()