import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Data
balance = 0
history = []

# Functions
def deposit():
    global balance
    amount = entry.get()
    if amount.isdigit():
        amount = int(amount)
        balance += amount
        history.append(f"Deposited: ₹{amount}")
        messagebox.showinfo("Success", f"Deposited ₹{amount}")
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Enter valid amount")

def withdraw():
    global balance
    amount = entry.get()
    if amount.isdigit():
        amount = int(amount)
        if amount <= balance:
            balance -= amount
            history.append(f"Withdrawn: ₹{amount}")
            messagebox.showinfo("Success", f"Withdrawn ₹{amount}")
            entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Insufficient balance")
    else:
        messagebox.showerror("Error", "Enter valid amount")

def check_balance():
    messagebox.showinfo("Balance", f"Current Balance: ₹{balance}")

def show_history():
    if history:
        messagebox.showinfo("History", "\n".join(history))
    else:
        messagebox.showinfo("History", "No transactions yet")

# GUI
root = tk.Tk()
root.title("VTU BANK")
root.geometry("400x500")

# ✅ LOGO CODE
try:
    img = Image.open("BANKING-SYSTEM/logo.png")   # make sure logo.png is in same folder
    img = img.resize((100, 100))
    logo = ImageTk.PhotoImage(img)

    logo_label = tk.Label(root, image=logo)
    logo_label.image = logo
    logo_label.pack(pady=10)

except Exception as e:
    print("Logo error:", e)

# Title
tk.Label(root, text="VTU BANK", font=("Arial", 18, "bold")).pack()
tk.Label(root, text="Welcome to VTU BANK").pack(pady=10)

# Entry
entry = tk.Entry(root)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Deposit", width=20, command=deposit).pack(pady=5)
tk.Button(root, text="Withdraw", width=20, command=withdraw).pack(pady=5)
tk.Button(root, text="Check Balance", width=20, command=check_balance).pack(pady=5)
tk.Button(root, text="Show History", width=20, command=show_history).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=10)

root.mainloop()