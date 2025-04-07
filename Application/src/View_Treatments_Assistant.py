import tkinter as tk
from tkinter import messagebox
import main_window as mw

def View_Treatments_Assistant(root, username, role, patients, users_data, treatments_report, treatments, doctors_report):
    root.destroy()

    root2 = tk.Tk()
    root2.title("Application")
    root2.geometry("800x600")

    listbox = tk.Listbox(width = 30, height = 10)
    listbox.place(x = 260, y = 0)

    if len(treatments) == 0:
        label = tk.Label(text = "No treatments available.")
        label.pack(padx=10, pady=10)
    else:
        for t in treatments:
            treatment_info = f"{t}"
            listbox.insert(tk.END, treatment_info)

    button = tk.Button(text = "Go Back", command = lambda: mw.go_back_to_main_window(root2, username, role, users_data, patients, treatments_report, treatments, doctors_report), width=14, height=2)
    button.place(x = 340, y = 550)

    root2.mainloop()
