from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk   # for resizing image

# ------------------ DATA ------------------
balance = 0
history = []

# ------------------ FUNCTIONS ------------------

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


# ------------------ GUI ------------------

root = Tk()
root.title("VTU BANK")
root.geometry("400x550")

# -------- LOGO (RESIZED) --------
try:
    img = Image.open("logo.png")
    img = img.resize((200, 200))   # resize here
    logo = ImageTk.PhotoImage(img)

    logo_label = Label(root, image=logo)
    logo_label.pack(pady=10)

except:
    print("Logo not found")

# -------- TITLE --------
Label(root, text="VTU BANK", font=("Arial", 20, "bold")).pack()
Label(root, text="Welcome to VTU BANK").pack(pady=5)

# -------- INPUT --------
entry = Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# -------- BUTTONS --------
Button(root, text="Deposit", width=20, command=deposit).pack(pady=5)
Button(root, text="Withdraw", width=20, command=withdraw).pack(pady=5)
Button(root, text="Check Balance", width=20, command=check_balance).pack(pady=5)
Button(root, text="Show History", width=20, command=show_history).pack(pady=5)
Button(root, text="Exit", width=20, command=root.quit).pack(pady=5)

# -------- RESULT --------
result_label = Label(root, text="", fg="green", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()