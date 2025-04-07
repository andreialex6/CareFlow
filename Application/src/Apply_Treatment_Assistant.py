import tkinter as tk
from tkinter import messagebox
import load_users as ls
import main_window as mw

def Apply_Treatment_Assistant(root, username, role, patients, users_data, treatments_report, treatments, doctors_report):
    root.destroy()

    root2 = tk.Tk()
    root2.title("Application")
    root2.geometry("800x600")

    label0 = tk.Label(text = "Name - Problem - Recommanded Treatment - Applied Treatment", font=("Helvetica", 14))
    label0.place(x = 150, y = 30)

    listbox = tk.Listbox(width = 60, height = 20)
    listbox.place(x = 140, y = 50)

    if patients:
        for usern in patients:
            for i in patients[usern]['Assistant']:
                if i == username:
                    if not patients[usern].get('applied_treatment'):
                        patients[usern]['applied_treatment'] = []
                    if patients[usern].get('recommanded_treatment'):
                        if len(patients[usern]['applied_treatment']) > 0:
                            patient_info = f"{usern} - {patients[usern]['problem']} - {patients[usern]['recommanded_treatment']} - {patients[usern]['applied_treatment']}"
                        else:
                            patient_info = f"{usern} - {patients[usern]['problem']} - {patients[usern]['recommanded_treatment']} - No treatment applied"
                    else:
                        patient_info = f"{usern} - {patients[usern]['problem']} - No treatment recommanded"
                    listbox.insert(tk.END, patient_info)
    else:
        # if there are no patients to display
        label = tk.Label(text = "No patients")
        label.pack(padx=10, pady=10)

    button1 = tk.Button(text = "Apply Treatment", command = lambda: Apply_Treatment(root2, patients, listbox, username, treatments_report, treatments, doctors_report), width=16, height=2)
    button1.place(x = 310, y = 500)

    button2 = tk.Button(text = "Go Back", command = lambda: mw.go_back_to_main_window(root2, username, role, users_data, patients, treatments_report, treatments, doctors_report), width=16, height=2)
    button2.place(x = 310, y = 550)

    root2.mainloop()

def Apply_Treatment(root2, patients, listbox, username, treatments_report, treatments, doctors_report):
    if listbox.size() == 0:
        tk.messagebox.showinfo("Information", "No Patients selected.")
    else:
        selection = listbox.curselection()
        if selection:
            index = selection[0]

            nr = 0
            ok = True

            for usern in patients:
                if ok == False:
                    break
                for i in patients[usern]['Assistant']:
                    if i == username:
                        if nr == index:
                            if patients[usern].get('recommanded_treatment'):
                                new_window = tk.Toplevel(root2)
                                new_window.title("Application")
                                new_window.geometry("400x400")

                                label1 = tk.Label(new_window, text = "Type treatment:")
                                label1.place(x = 160, y = 20)
                                entry1 = tk.Entry(new_window, width = 20)
                                entry1.place(x = 120, y = 40)

                                aux = usern
                                button = tk.Button(new_window, text = "Apply Treatment", command = lambda: Apply_Treatment_click(entry1), width=12, height=2)
                                button.place(x = 150, y = 80)

                                def Apply_Treatment_click(entry1):
                                    treatment = entry1.get()

                                    # if treatment is available and is also recommanded by a doctor
                                    if treatment in treatments and treatment in patients[aux]['recommanded_treatment'] and treatment not in patients[aux]['applied_treatment']:
                                        patients[aux]['applied_treatment'].append(treatment)
                                        if aux not in treatments_report:
                                            treatments_report[aux] = {"treatments": []}
                                        treatments_report[aux]["treatments"].append({"treatment": treatment, "assistant": username})
                                        ls.update_treatments(treatments_report)

                                        ls.update_patients(patients)
                                        tk.messagebox.showinfo("Information", "Applied treatment.")
                                    elif treatment not in patients[aux]['recommanded_treatment']:
                                        tk.messagebox.showinfo("Information", "Treatment not recommanded by a doctor.")
                                    elif treatment not in treatments:
                                        tk.messagebox.showinfo("Information", "Treatment not available.")
                                    elif treatment in patients[aux]['applied_treatment']:
                                        tk.messagebox.showinfo("Information", "Treatment already applied.")
                                    new_window.destroy()
                            else:
                                tk.messagebox.showinfo("Information", "You can't apply treatment to a patient with no treatment recommanded.")
                            # listbox.insert(tk.END, patient_info)
                            ok = False
                            break
                        nr = nr + 1
        else:
            tk.messagebox.showinfo("Information", "No Patients selected.")
