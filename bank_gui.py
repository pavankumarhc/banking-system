import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# ---------------- FUNCTIONS ---------------- #

balance = 0
history = []

def deposit():
    global balance
    try:
        amt = float(entry.get())
        balance += amt
        history.append(f"Deposited: ₹{amt}")
        messagebox.showinfo("Success", f"Deposited ₹{amt}")
        entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Enter valid amount")

def withdraw():
    global balance
    try:
        amt = float(entry.get())
        if amt > balance:
            messagebox.showerror("Error", "Insufficient Balance")
        else:
            balance -= amt
            history.append(f"Withdrawn: ₹{amt}")
            messagebox.showinfo("Success", f"Withdrawn ₹{amt}")
        entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Enter valid amount")

def check_balance():
    messagebox.showinfo("Balance", f"Your Balance: ₹{balance}")

def show_history():
    if history:
        messagebox.showinfo("History", "\n".join(history))
    else:
        messagebox.showinfo("History", "No transactions yet")

def exit_app():
    root.destroy()

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("VTU BANK")
root.geometry("400x500")

# ✅ LOGO FIX (Dynamic Path)
try:
    base_path = os.path.dirname(__file__)
    img_path = os.path.join(base_path, "logo.png")

    img = Image.open(img_path)
    img = img.resize((80, 80))
    logo = ImageTk.PhotoImage(img)

    logo_label = tk.Label(root, image=logo)
    logo_label.image = logo
    logo_label.pack(pady=10)

except Exception as e:
    print("LOGO ERROR:", e)

# Title
tk.Label(root, text="VTU BANK", font=("Arial", 20, "bold")).pack()
tk.Label(root, text="Welcome to VTU BANK").pack(pady=5)

# Entry
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Deposit", width=20, command=deposit).pack(pady=5)
tk.Button(root, text="Withdraw", width=20, command=withdraw).pack(pady=5)
tk.Button(root, text="Check Balance", width=20, command=check_balance).pack(pady=5)
tk.Button(root, text="Show History", width=20, command=show_history).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=exit_app).pack(pady=10)

root.mainloop()