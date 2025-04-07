import tkinter as tk
from tkinter import messagebox
import load_users as ls
import main_window as mw
import load_treatments as lt

def Manage_Treatment(root, username, role, patients, users_data, treatments_report, treatments, doctors_report):
    root.destroy()

    root2 = tk.Tk()
    root2.title("Application")
    root2.geometry("800x600")

    listbox = tk.Listbox(width = 30, height = 10)
    listbox.place(x = 260, y = 0)

    if len(treatments) == 0:
        label = tk.Label(text = "No treatments available.")
        label.pack(padx=10, pady=10)
        treatments = []
    else:
        for t in treatments:
            treatment_info = f"{t}"
            listbox.insert(tk.END, treatment_info)

    button1 = tk.Button(text = "Add a treatment", command = lambda: Add_Treatment(root2, users_data, treatments, listbox), width=14, height=2)
    button1.place(x = 340, y = 450)

    button2 = tk.Button(text = "Remove a treatment", command = lambda: Remove_Treatment(users_data, treatments, listbox), width=14, height=2)
    button2.place(x = 340, y = 500)

    button3 = tk.Button(text = "Go Back", command = lambda: mw.go_back_to_main_window(root2, username, role, users_data, patients, treatments_report, treatments, doctors_report), width=14, height=2)
    button3.place(x = 340, y = 550)

    root2.mainloop()

def Add_Treatment(root, users_data, treatments, listbox):
    new_window = tk.Toplevel(root)
    new_window.title("Application")
    new_window.geometry("400x400")

    label = tk.Label(new_window, text = "Type treatment:")
    label.place(x = 152, y = 20)
    entry = tk.Entry(new_window, width = 20)
    entry.place(x = 120, y = 40)

    button = tk.Button(new_window, text = "Add Treatment", command = lambda: Add_Treatment_click(entry), width = 10, height = 2)
    button.place(x = 150, y = 170)

    def Add_Treatment_click(entry):
        treatment = entry.get()

        if treatment in treatments:
            tk.messagebox.showinfo("Information", "Treatment already added.")    
        else:
            treatments.append(treatment)
            lt.save_treatments(treatments)
            tk.messagebox.showinfo("Information", "Added a treatment.")
        
        new_window.destroy()

def Remove_Treatment(users_data, treatments, listbox):
    if listbox.size() == 0:
        tk.messagebox.showinfo("Information", "No treatments.")
    else:
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            listbox.delete(index)

            del treatments[index]
            lt.save_treatments(treatments)
        else:
            tk.messagebox.showinfo("Information", "No treatments selected to remove.")
