import tkinter as tk
from tkinter import messagebox
import main_window as mw

def login(users_data, patients, treatments_report, treatments, doctors_report):
    root = tk.Tk()
    root.title("Application")
    root.geometry("800x600")

    # login label
    label1 = tk.Label(text = "Login", font=("Helvetica", 20))
    label1.place(x = 360, y = 100)

    # username label
    label2 = tk.Label(text = "Username:", font=("Helvetica", 10))
    label2.place(x = 360, y = 140)

    # username entry
    entry1 = tk.Entry(width = 14)
    entry1.place(x = 330, y = 160)

    # password label
    label3 = tk.Label(text = "Password:", font=("Helvetica", 10))
    label3.place(x = 360, y = 190)

    # password entry
    entry2 = tk.Entry(width = 14, show = "*")
    entry2.place(x = 330, y = 210)

    # login button
    button = tk.Button(text = "Login", command = lambda: Login_button(root, entry1, entry2, users_data, patients, treatments_report, treatments, doctors_report), width = 7, height = 2)
    button.place(x = 353, y = 240)

    root.mainloop()

def Login_button(root, entry1, entry2, users_data, patients, treatments_report, treatments, doctors_report):
    username = entry1.get()
    password = entry2.get()

    if not username or not password:
        tk.messagebox.showinfo("Info", "You must complete all fields!")
        return

    if username in users_data and users_data[username]["password"] == password:
        tk.messagebox.showinfo("Info", "Connected!")
        # close login window
        root.destroy()
        # go on main window
        mw.main_window(username, users_data[username]["role"], users_data, patients, treatments_report, treatments, doctors_report)
        return
    else:
        tk.messagebox.showinfo("Info", "Incorrect credentials!")
        return
