import tkinter as tk
from tkinter import messagebox
import load_users as ls
import main_window as mw

# function to list all patients and to decide which action is next
def Manage_Patients(root, username, role, patients, users_data, treatments_report, treatments, doctors_report):
    root.destroy()

    root2 = tk.Tk()
    root2.title("Application")
    root2.geometry("800x600")

    label0 = tk.Label(text = "Name - Problem", font=("Helvetica", 14))
    label0.place(x = 340, y = 30)

    listbox = tk.Listbox(width = 50, height = 14)
    listbox.place(x = 180, y = 50)

    if patients:
        for usern in patients:
            patient_info = f"{usern} - {patients[usern]['problem']}"
            listbox.insert(tk.END, patient_info)
    else:
        # if there are no patients to display
        label = tk.Label(text = "No patients")
        label.pack(padx=10, pady=60)

    button1 = tk.Button(text = "Add a patient", command = lambda: Add_Patient(root2, patients, listbox), width=10, height=2)
    button1.place(x = 340, y = 400)

    button2 = tk.Button(text = "Update a patient", command = lambda: Update_Patient(root2, patients, listbox), width=10, height=2)
    button2.place(x = 340, y = 450)

    button3 = tk.Button(text = "Remove a patient", command = lambda: Remove_Patient(patients, listbox), width=10, height=2)
    button3.place(x = 340, y = 500)

    button4 = tk.Button(text = "Go Back", command = lambda: mw.go_back_to_main_window(root2, username, role, users_data, patients, treatments_report, treatments, doctors_report), width=10, height=2)
    button4.place(x = 340, y = 550)

    root2.mainloop()

# function to add a patient
def Add_Patient(root, patients, listbox):
    new_window = tk.Toplevel(root)
    new_window.title("Application")
    new_window.geometry("400x400")

    label1 = tk.Label(new_window, text = "Type name:")
    label1.place(x = 152, y = 20)
    entry1 = tk.Entry(new_window, width = 20)
    entry1.place(x = 120, y = 40)

    label2 = tk.Label(new_window, text = "Type problem:")
    label2.place(x = 152, y = 65)
    entry2 = tk.Entry(new_window, width = 20)
    entry2.place(x = 120, y = 85)

    button = tk.Button(new_window, text = "Add Patient", command = lambda: Add_Patient_click(entry1, entry2), width = 10, height = 2)
    button.place(x = 150, y = 170)

    def Add_Patient_click(entry1, entry2):
        username = entry1.get()
        problem = entry2.get()

        patients[username] = {
            "problem": problem
        }

        ls.update_patients(patients)
        tk.messagebox.showinfo("Information", "Added a patient.")
        new_window.destroy()

# function to update a patient
def Update_Patient(root2, patients, listbox):
    if listbox.size() == 0:
        tk.messagebox.showinfo("Information", "No Patients.")
    else:
        selection = listbox.curselection()
        if selection:
            index = selection[0]

            nr = 0
            # search for the patient to update
            for usrn in patients:
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

            label2 = tk.Label(new_window, text = "Type problem:")
            label2.place(x = 152, y = 65)
            entry2 = tk.Entry(new_window, width = 20)
            entry2.place(x = 120, y = 85)

            button = tk.Button(new_window, text = "Update Patient", command = lambda: Update_Patient_click(entry1, entry2, usrn), width = 10, height = 2)
            button.place(x = 150, y = 170)

            def Update_Patient_click(entry1, entry2, usrn):
                username = entry1.get()
                problem = entry2.get()

                patients[username] = patients.pop(usrn)
                patients[username] = {
                    "problem": problem
                }

                ls.update_patients(patients)
                tk.messagebox.showinfo("Information", "Updated a patient.")
                new_window.destroy()
        else:
            tk.messagebox.showinfo("Information", "No Patients selected to update.")

# function to remove a patient
def Remove_Patient(patients, listbox):
    if listbox.size() == 0:
        tk.messagebox.showinfo("Information", "No Patients.")
    else:
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            listbox.delete(index)
            nr = 0
            # search for the user to delete
            for usrn in patients:
                if nr == index:
                    # remove user from dictionary
                    del patients[usrn]
                    # update json to remove patient from json
                    ls.update_patients(patients)
                    break
                nr = nr + 1
        else:
            tk.messagebox.showinfo("Information", "No Patients selected to remove.")
