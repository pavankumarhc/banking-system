from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# ------------------ DATA ------------------
balance = 0
history = []

BG_COLOR = "#0f172a"       # dark background
CARD_COLOR = "#1e293b"     # card color
BTN_COLOR = "#22c55e"      # green button
TEXT_COLOR = "white"

# ------------------ LOGIN ------------------

def login():
    if user_entry.get() == "admin" and pass_entry.get() == "1234":
        login_window.destroy()
        open_bank()
    else:
        messagebox.showerror("Error", "Invalid Login")

# ------------------ BANK FUNCTIONS ------------------

def deposit():
    global balance
    try:
        amount = int(entry.get())
        if amount <= 0:
            raise ValueError

        balance += amount
        history.append(f"+ ₹{amount}")
        result_label.config(text=f"Deposited ₹{amount}")
        update_balance()

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
            history.append(f"- ₹{amount}")
            result_label.config(text=f"Withdrawn ₹{amount}")
            update_balance()

    except:
        messagebox.showerror("Error", "Enter valid amount")


def update_balance():
    balance_label.config(text=f"₹ {balance}")


def show_history():
    if not history:
        result_label.config(text="No transactions")
    else:
        result_label.config(text="\n".join(history[-5:]))


# ------------------ BANK UI ------------------

def open_bank():
    global entry, result_label, balance_label

    root = Tk()
    root.title("VTU BANK")
    root.geometry("400x600")
    root.configure(bg=BG_COLOR)

    # -------- LOGO --------
    try:
        img = Image.open("logo.png").resize((120, 120))
        logo = ImageTk.PhotoImage(img)

        Label(root, image=logo, bg=BG_COLOR).pack(pady=10)
        root.logo = logo
    except:
        pass

    # -------- TITLE --------
    Label(root, text="VTU BANK", fg=TEXT_COLOR, bg=BG_COLOR,
          font=("Arial", 20, "bold")).pack()

    # -------- BALANCE CARD --------
    frame = Frame(root, bg=CARD_COLOR, padx=20, pady=20)
    frame.pack(pady=15, padx=20, fill="x")

    Label(frame, text="Current Balance", fg="lightgray",
          bg=CARD_COLOR).pack()

    balance_label = Label(frame, text="₹ 0", fg=BTN_COLOR,
                          bg=CARD_COLOR, font=("Arial", 24, "bold"))
    balance_label.pack()

    # -------- INPUT --------
    entry = Entry(root, font=("Arial", 14), justify="center")
    entry.pack(pady=15, ipadx=10, ipady=5)

    # -------- BUTTON STYLE --------
    def styled_button(text, cmd):
        return Button(root, text=text, command=cmd,
                      bg=BTN_COLOR, fg="black",
                      font=("Arial", 11, "bold"),
                      width=20, pady=5)

    styled_button("Deposit", deposit).pack(pady=5)
    styled_button("Withdraw", withdraw).pack(pady=5)
    styled_button("Check Balance", update_balance).pack(pady=5)
    styled_button("Transaction History", show_history).pack(pady=5)

    Button(root, text="Exit", command=root.quit,
           bg="red", fg="white", width=20).pack(pady=10)

    # -------- RESULT --------
    result_label = Label(root, text="", fg="white",
                         bg=BG_COLOR, font=("Arial", 11))
    result_label.pack(pady=10)

    root.mainloop()


# ------------------ LOGIN UI ------------------

login_window = Tk()
login_window.title("VTU BANK LOGIN")
login_window.geometry("300x300")
login_window.configure(bg=BG_COLOR)

Label(login_window, text="VTU BANK", fg="white", bg=BG_COLOR,
      font=("Arial", 18, "bold")).pack(pady=20)

user_entry = Entry(login_window)
user_entry.pack(pady=10, ipadx=10, ipady=5)

pass_entry = Entry(login_window, show="*")
pass_entry.pack(pady=10, ipadx=10, ipady=5)

Button(login_window, text="Login", command=login,
       bg=BTN_COLOR, width=15).pack(pady=20)

login_window.mainloop()