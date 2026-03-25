import tkinter as tk
from tkinter import messagebox
import bank_gui   # your main file

# correct login details
USERNAME = "admin"
PASSWORD = "1234"

def login():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Success", "Login Successful")
        root.destroy()
        bank_gui.main()   # open your banking system
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

root = tk.Tk()
root.title("VTU BANK Login")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()