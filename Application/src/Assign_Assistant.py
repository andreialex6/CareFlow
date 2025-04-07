import tkinter as tk
from tkinter import messagebox
import load_users as ls
import main_window as mw

def Assign_Assistant(root, username, role, users_data, patients, treatments_report, treatments, doctors_report):
    root.destroy()

    root2 = tk.Tk()
    root2.title("Application")
    root2.geometry("800x600")

    label0 = tk.Label(text = "Assistants' name", font=("Helvetica", 14))
    label0.place(x = 350, y = 10)

    listbox = tk.Listbox(width = 30, height = 10)
    listbox.place(x = 280, y = 30)

    found_assistants = False
    for usern in users_data:
        if users_data[usern]["role"] == "Assistant":
            found_assistants = True
            assistant_info = f"{usern}"
            listbox.insert(tk.END, assistant_info)

    # if there are no assistants to display
    if found_assistants == False:
        label = tk.Label(text = "No assistants")
        label.pack(padx=10, pady=10)

    label1 = tk.Label(text = "Patient's name - Assistant", font=("Helvetica", 14))
    label1.place(x = 320, y = 220)

    listbox1 = tk.Listbox(width = 60, height = 10)
    listbox1.place(x = 140, y = 250)

    label2 = tk.Label(text = "Select a patient to assign/delete assistant", font=("Helvetica", 14))
    label2.place(x = 250, y = 440)

    if patients:
        for usern in patients:
            if patients[usern].get('Assistant'):
                if len(patients[usern]['Assistant']) > 0:
                    patient_info = f"{usern} - {patients[usern]['Assistant']}"
                else:
                    patient_info = f"{usern} - No assistant assigned"
            else:
                patients[usern]['Assistant'] = []
                if len(patients[usern]['Assistant']) > 0:
                    patient_info = f"{usern} - {patients[usern]['Assistant']}"
                else:
                    patient_info = f"{usern} - No assistant assigned"
            listbox1.insert(tk.END, patient_info)
    else:
        # if there are no patients to display
        label1 = tk.Label(text = "No patients")
        label1.pack(padx=180, pady=260)

    button1 = tk.Button(text = "Assign assistant", command = lambda: Assign_Assistant_click(root2, patients, listbox1, users_data), width=14, height=1)
    button1.place(x = 330, y = 490)

    button2 = tk.Button(text = "Delete assistant", command = lambda: Delete_Assistant_click(root2, patients, listbox1, users_data), width=14, height=1)
    button2.place(x = 330, y = 520)

    button2 = tk.Button(text = "Go Back", command = lambda: mw.go_back_to_main_window(root2, username, role, users_data, patients, treatments_report, treatments, doctors_report), width=14, height=1)
    button2.place(x = 330, y = 550)

def Assign_Assistant_click(root2, patients, listbox, users_data):
    if listbox.size() == 0:
        tk.messagebox.showinfo("Information", "No Patients selected.")
    else:
        selection = listbox.curselection()
        if selection:
            index = selection[0]

            nr = 0
            # search for the patient
            for usrn in patients:
                if nr == index:
                    break
                nr = nr + 1

            new_window = tk.Toplevel(root2)
            new_window.title("Application")
            new_window.geometry("400x400")

            label1 = tk.Label(new_window, text = "Type assistant's username:")
            label1.place(x = 120, y = 20)
            entry1 = tk.Entry(new_window, width = 20)
            entry1.place(x = 120, y = 40)

            button = tk.Button(new_window, text = "Assign assistant", command = lambda: Assign_Assistant_click2(entry1, usrn), width = 10, height = 2)
            button.place(x = 150, y = 170)

            def Assign_Assistant_click2(entry1, usrn):
                assistant = entry1.get()

                exist_assistant = False

                if assistant in users_data:
                    if users_data[assistant]['role'] == "Assistant":
                        exist_assistant = True

                if exist_assistant == True:
                    already_assigned = False
                    for i in patients[usrn]["Assistant"]:
                        if assistant == i:
                            tk.messagebox.showinfo("Information", "Assistant already assigned.")
                            already_assigned = True
                            break
                    if already_assigned == False:
                        # check if "Assistant" is a list or we have
                        # to make it because a patient can have more assistants
                        if isinstance(patients[usrn]["Assistant"], list):
                            patients[usrn]["Assistant"].append(assistant)
                        else:
                            patients[usrn]["Assistant"] = [patients[usrn]["Assistant"], assistant]
                        ls.update_patients(patients)
                        tk.messagebox.showinfo("Information", "Assigned an assistant.")
                        new_window.destroy()
                else:
                    tk.messagebox.showinfo("Information", "Invalid assistant.")
        else:
            tk.messagebox.showinfo("Information", "No Patients selected.")

def Delete_Assistant_click(root2, patients, listbox, users_data):
    if listbox.size() == 0:
        tk.messagebox.showinfo("Information", "No Patients selected.")
    else:
        selection = listbox.curselection()
        if selection:
            index = selection[0]

            nr = 0
            # search for the patient
            for usrn in patients:
                if nr == index:
                    break
                nr = nr + 1

            new_window = tk.Toplevel(root2)
            new_window.title("Application")
            new_window.geometry("400x400")

            label1 = tk.Label(new_window, text = "Type assistant's username:")
            label1.place(x = 120, y = 20)
            entry1 = tk.Entry(new_window, width = 20)
            entry1.place(x = 120, y = 40)

            button = tk.Button(new_window, text = "Delete assistant", command = lambda: Delete_Assistant_click2(entry1, usrn), width = 10, height = 2)
            button.place(x = 150, y = 170)

            def Delete_Assistant_click2(entry1, usrn):
                assistant = entry1.get()

                exist_assistant = False

                if assistant in users_data:
                    if users_data[assistant]['role'] == "Assistant":
                        exist_assistant = True

                if exist_assistant == True:
                    # check if "Assistant" is a list or we have
                    # to make it because a patient can have more assistants
                    if isinstance(patients[usrn]["Assistant"], list):
                        try:
                            patients[usrn]["Assistant"].remove(assistant)
                            tk.messagebox.showinfo("Information", "Removed an assistant.")
                            ls.update_patients(patients)
                        except ValueError:
                            tk.messagebox.showinfo("Information", "Assistant not assigned to this patient.")
                    else:
                        patients[usrn]["Assistant"] = [patients[usrn]["Assistant"]]
                        try:
                            patients[usrn]["Assistant"].remove(assistant)
                            tk.messagebox.showinfo("Information", "Removed an assistant.")
                            ls.update_patients(patients)
                        except ValueError:
                            tk.messagebox.showinfo("Information", "Assistant not assigned to this patient.")
                    new_window.destroy()
                else:
                    tk.messagebox.showinfo("Information", "Invalid assistant username.")
        else:
            tk.messagebox.showinfo("Information", "No Patients selected.")
