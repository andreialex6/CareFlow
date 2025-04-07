import tkinter as tk
from tkinter import messagebox
import load_users as ls
import main_window as mw

# function to list all patients, problems and treatments for them
def Recommand_Treatment_Doctor(root, username, role, patients, users_data, treatments_report, treatments, doctors_report):
    root.destroy()

    root2 = tk.Tk()
    root2.title("Application")
    root2.geometry("800x600")

    label0 = tk.Label(text = "Name - Problem - Recommanded Treatment", font=("Helvetica", 14))
    label0.place(x = 220, y = 30)

    listbox = tk.Listbox(width = 60, height = 20)
    listbox.place(x = 140, y = 50)

    if patients:
        for usern in patients:
            if patients[usern].get('recommanded_treatment'):
                patient_info = f"{usern} - {patients[usern]['problem']} - {patients[usern]['recommanded_treatment']}"
            else:
                patients[usern]['recommanded_treatment'] = []
                patient_info = f"{usern} - {patients[usern]['problem']} - No treatment recommanded"
            listbox.insert(tk.END, patient_info)
    else:
        # if there are no patients to display
        label = tk.Label(text = "No patients")
        label.pack(padx=10, pady=10)

    button1 = tk.Button(text = "Recommand Treatment", command = lambda: Recommand_Treatment(root2, patients, listbox, treatments, doctors_report, username), width=16, height=2)
    button1.place(x = 310, y = 500)

    button2 = tk.Button(text = "Go Back", command = lambda: mw.go_back_to_main_window(root2, username, role, users_data, patients, treatments_report, treatments, doctors_report), width=16, height=2)
    button2.place(x = 310, y = 550)

    root2.mainloop()

# function to recommand treatment
def Recommand_Treatment(root2, patients, listbox, treatments, doctors_report, username):
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

            label1 = tk.Label(new_window, text = "Recommand treatment:")
            label1.place(x = 130, y = 20)
            entry1 = tk.Entry(new_window, width = 20)
            entry1.place(x = 120, y = 40)

            button = tk.Button(new_window, text = "Recommand treatment", command = lambda: Recommand_Treatment_click(entry1, usrn), width = 15, height = 2)
            button.place(x = 120, y = 170)

            def Recommand_Treatment_click(entry1, usrn):
                treatment = entry1.get()

                if treatment in treatments:
                    patients[usrn]['recommanded_treatment'].append(treatment)

                    if username not in doctors_report:
                        doctors_report[username] = {"recommanded_treatments": []}
                    doctors_report[username]['recommanded_treatments'].append({"patient": usrn, "recommanded_treatment": treatment})
                    ls.update_doctors_report(doctors_report)

                    ls.update_patients(patients)
                    tk.messagebox.showinfo("Information", "Added treatment.")
                else:
                    tk.messagebox.showinfo("Information", "This treatment is not available.")
                new_window.destroy()
        else:
            tk.messagebox.showinfo("Information", "No patient selected.")
