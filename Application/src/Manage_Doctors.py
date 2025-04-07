import tkinter as tk
from tkinter import messagebox
import load_users as ls
import main_window as mw

# function to list all doctors and to decide which action is next
def Manage_Doctors(root, username, role, users_data, patients, treatments_report, treatments, doctors_report):
    root.destroy()

    root2 = tk.Tk()
    root2.title("Application")
    root2.geometry("800x600")

    listbox = tk.Listbox(width = 30, height = 10)
    listbox.place(x = 260, y = 0)

    found_doctors = False
    for usern in users_data:
        if users_data[usern]["role"] == "Doctor":
            found_doctors = True
            doctor_info = f"{usern}"
            listbox.insert(tk.END, doctor_info)

    # if there are no doctors to display
    if found_doctors == False:
        label = tk.Label(text = "No doctors")
        label.pack(padx=10, pady=10)

    button1 = tk.Button(text = "Add a doctor", command = lambda: Add_Doctor(root2, users_data, listbox), width=10, height=2)
    button1.place(x = 340, y = 400)

    button2 = tk.Button(text = "Update a doctor", command = lambda: Update_Doctor(root2, users_data, listbox), width=10, height=2)
    button2.place(x = 340, y = 450)

    button3 = tk.Button(text = "Remove a doctor", command = lambda: Remove_Doctor(users_data, listbox), width=10, height=2)
    button3.place(x = 340, y = 500)

    button4 = tk.Button(text = "Go Back", command = lambda: mw.go_back_to_main_window(root2, username, role, users_data, patients, treatments_report, treatments, doctors_report), width=10, height=2)
    button4.place(x = 340, y = 550)

    root2.mainloop()

# function to add a doctor
def Add_Doctor(root, users_data, listbox):
    new_window = tk.Toplevel(root)
    new_window.title("Application")
    new_window.geometry("400x400")

    label1 = tk.Label(new_window, text = "Type username:")
    label1.place(x = 152, y = 20)
    entry1 = tk.Entry(new_window, width = 20)
    entry1.place(x = 120, y = 40)

    label2 = tk.Label(new_window, text = "Type password:")
    label2.place(x = 152, y = 65)
    entry2 = tk.Entry(new_window, width = 20)
    entry2.place(x = 120, y = 85)

    button = tk.Button(new_window, text = "Add Doctor", command = lambda: Add_Doctor_click(entry1, entry2), width = 10, height = 2)
    button.place(x = 150, y = 170)

    def Add_Doctor_click(entry1, entry2):
        username = entry1.get()
        password = entry2.get()

        users_data[username] = {
            "password": password,
            "role": "Doctor"
        }

        ls.update_users(users_data)
        tk.messagebox.showinfo("Information", "Added a doctor.")
        new_window.destroy()

# function to update a doctor
def Update_Doctor(root2, users_data, listbox):
    if listbox.size() == 0:
        tk.messagebox.showinfo("Information", "No Doctors.")
    else:
        selection = listbox.curselection()
        if selection:
            index = selection[0]

            nr = 0
            # search for the user to update
            for usrn in users_data:
                if users_data[usrn]["role"] == "Doctor":
                    if nr == index:
                        break
                    nr = nr + 1

            new_window = tk.Toplevel(root2)
            new_window.title("Application")
            new_window.geometry("400x400")

            label1 = tk.Label(new_window, text = "Type username:")
            label1.place(x = 152, y = 20)
            entry1 = tk.Entry(new_window, width = 20)
            entry1.place(x = 120, y = 40)

            label2 = tk.Label(new_window, text = "Type password:")
            label2.place(x = 152, y = 65)
            entry2 = tk.Entry(new_window, width = 20)
            entry2.place(x = 120, y = 85)

            button = tk.Button(new_window, text = "Update Doctor", command = lambda: Update_Doctor_click(entry1, entry2, usrn), width = 10, height = 2)
            button.place(x = 150, y = 170)

            def Update_Doctor_click(entry1, entry2, usrn):
                username = entry1.get()
                password = entry2.get()

                users_data[username] = users_data.pop(usrn)
                users_data[username] = {
                    "password": password,
                    "role": "Doctor"
                }

                ls.update_users(users_data)
                tk.messagebox.showinfo("Information", "Updated a doctor.")
                new_window.destroy()
        else:
            tk.messagebox.showinfo("Information", "No Doctors selected to update.")

# function to remove a doctor
def Remove_Doctor(users_data, listbox):
    if listbox.size() == 0:
        tk.messagebox.showinfo("Information", "No Doctors.")
    else:
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            listbox.delete(index)
            nr = 0
            # search for the user to delete
            for usrn in users_data:
                if users_data[usrn]["role"] == "Doctor":
                    if nr == index:
                        # remove user from dictionary
                        del users_data[usrn]
                        # update json to remove user from json
                        ls.update_users(users_data)
                        break
                    nr = nr + 1
        else:
            tk.messagebox.showinfo("Information", "No Doctors selected to remove.")
