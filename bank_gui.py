from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# ------------------ DATA ------------------
balance = 0
history = []

# ------------------ LOGIN FUNCTION ------------------

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "1234":
        login_window.destroy()
        open_bank()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


# ------------------ BANK FUNCTIONS ------------------

def deposit():
    global balance
    try:
        amount = int(entry.get())
        if amount <= 0:
            raise ValueError

        balance += amount
        history.append(f"Deposited ₹{amount}")
        result_label.config(text=f"Deposited: ₹{amount}")
        entry.delete(0, END)

    except:
        messagebox.showerror("Error", "Enter valid amount")


def withdraw():
    global balance
    try:
        amount = int(entry.get())

        if amount > balance:
            result_label.config(text="Insufficient Balance")
        else:
            balance -= amount
            history.append(f"Withdrawn ₹{amount}")
            result_label.config(text=f"Withdrawn: ₹{amount}")

        entry.delete(0, END)

    except:
        messagebox.showerror("Error", "Enter valid amount")


def check_balance():
    result_label.config(text=f"Balance: ₹{balance}")


def show_history():
    if not history:
        result_label.config(text="No transactions yet")
    else:
        result_label.config(text="\n".join(history))


# ------------------ BANK WINDOW ------------------

def open_bank():
    global entry, result_label

    root = Tk()
    root.title("VTU BANK")
    root.geometry("400x550")

    # Logo
    try:
        img = Image.open("logo.png")
        img = img.resize((200, 200))
        logo = ImageTk.PhotoImage(img)

        logo_label = Label(root, image=logo)
        logo_label.image = logo
        logo_label.pack(pady=10)
    except:
        pass

    Label(root, text="VTU BANK", font=("Arial", 20, "bold")).pack()
    Label(root, text="Welcome to VTU BANK").pack(pady=5)

    entry = Entry(root, font=("Arial", 14))
    entry.pack(pady=10)

    Button(root, text="Deposit", width=20, command=deposit).pack(pady=5)
    Button(root, text="Withdraw", width=20, command=withdraw).pack(pady=5)
    Button(root, text="Check Balance", width=20, command=check_balance).pack(pady=5)
    Button(root, text="Show History", width=20, command=show_history).pack(pady=5)
    Button(root, text="Exit", width=20, command=root.quit).pack(pady=5)

    result_label = Label(root, text="", fg="green", font=("Arial", 12))
    result_label.pack(pady=10)

    root.mainloop()


# ------------------ LOGIN WINDOW ------------------

login_window = Tk()
login_window.title("VTU BANK LOGIN")
login_window.geometry("300x250")

Label(login_window, text="Login", font=("Arial", 18, "bold")).pack(pady=10)

Label(login_window, text="Username").pack()
user_entry = Entry(login_window)
user_entry.pack(pady=5)

Label(login_window, text="Password").pack()
pass_entry = Entry(login_window, show="*")
pass_entry.pack(pady=5)

Button(login_window, text="Login", width=15, command=login).pack(pady=15)

login_window.mainloop()