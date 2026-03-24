import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ---------- BALANCE ----------

def get_balance():
    if not os.path.exists("balance.txt"):
        return 0
    with open("balance.txt", "r") as f:
        data = f.read().strip()
        return int(data) if data else 0

def set_balance(balance):
    with open("balance.txt", "w") as f:
        f.write(str(balance))

# ---------- HISTORY ----------

def add_history(action, amount, balance):
    time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
    with open("history.txt", "a") as f:
        f.write(f"{time}|{action}|{amount}|{balance}\n")

def show_history():
    try:
        with open("history.txt", "r") as f:
            data = f.read()
            if not data:
                messagebox.showinfo("History", "No transactions yet")
            else:
                messagebox.showinfo("Transaction History", data)
    except:
        messagebox.showinfo("History", "No history found")

# ---------- OPERATIONS ----------

def deposit():
    try:
        amount = int(entry.get())
        if amount <= 0:
            messagebox.showerror("Error", "Enter positive amount")
            return

        bal = get_balance()
        bal += amount
        set_balance(bal)
        add_history("Deposit", amount, bal)

        messagebox.showinfo("Success", "Deposit successful")
        entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Enter valid number")

def withdraw():
    try:
        amount = int(entry.get())
        if amount <= 0:
            messagebox.showerror("Error", "Enter positive amount")
            return

        bal = get_balance()

        if amount > bal:
            messagebox.showerror("Error", "Insufficient balance")
            return

        bal -= amount
        set_balance(bal)
        add_history("Withdraw", amount, bal)

        messagebox.showinfo("Success", "Withdrawal successful")
        entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Enter valid number")

def check_balance():
    bal = get_balance()
    messagebox.showinfo("Balance", f"Current Balance: ₹{bal}")

# ---------- GUI ----------

root = tk.Tk()
root.title("VTU BANK")
root.geometry("400x500")
root.resizable(False, False)

# Logo
try:
    img = Image.open("logo.png")
    img = img.resize((120, 120))
    photo = ImageTk.PhotoImage(img)

    label_logo = tk.Label(root, image=photo)
    label_logo.pack(pady=10)
except:
    tk.Label(root, text="🏦 VTU BANK", font=("Arial", 20)).pack(pady=10)

# Title
tk.Label(root, text="VTU BANK", font=("Arial", 18, "bold")).pack()

# Entry
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=15)

# Buttons
tk.Button(root, text="Deposit", width=20, command=deposit).pack(pady=5)
tk.Button(root, text="Withdraw", width=20, command=withdraw).pack(pady=5)
tk.Button(root, text="Check Balance", width=20, command=check_balance).pack(pady=5)
tk.Button(root, text="Show History", width=20, command=show_history).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=15)

root.mainloop()