import tkinter as tk
from tkinter import messagebox
import login as lg
import Manage_Doctors as MD
import Manage_Assistants as MA
import Manage_Patients as MP
import Recommand_Treatment_Doctor as MTD
import Apply_Treatment_Assistant as MTA
import Assign_Assistant as AA
import Download_Patients_Report as DPR
import Manage_Treatment as MT
import View_Treatments_Assistant as VTA

def main_window(username, role, users_data, patients, treatments_report, treatments, doctors_report):
    root = tk.Tk()
    root.title("Application")
    root.geometry("800x600")

    # role and username label
    label1 = tk.Label(text = role + " " + username, font=("Helvetica", 14))
    label1.place(x = 12, y = 12)

    # Sign Out button
    button0 = tk.Button(text = "Sign Out", command = lambda: Sign_Out(root, users_data, patients, treatments_report, treatments, doctors_report), width = 10, height = 1)
    button0.place(x = 670, y = 10)

    if role == "Manager" or role == "Doctor":
        # manage patients button
        button0 = tk.Button(text = "Download Patients Report", command = lambda: DPR.Download_Patients_Report(), width = 18, height = 4)
        button0.place(x = 90, y = 410)

    if role == "Manager":
        # manage patients button
        button02 = tk.Button(text = "Download Doctors Report", command = lambda: DPR.Download_Doctors_Report(), width = 18, height = 4)
        button02.place(x = 90, y = 500)

    if role == "Manager" or role == "Doctor":
        # manage patients button
        button1 = tk.Button(text = "Manage Patients", command = lambda: MP.Manage_Patients(root, username, role, patients, users_data, treatments_report, treatments, doctors_report), width = 16, height = 4)
        button1.place(x = 335, y = 140)

    if role == "Manager" or role == "Doctor":
        # manage treatment button
        button2 = tk.Button(text = "Manage Treatments", command = lambda: MT.Manage_Treatment(root, username, role, patients, users_data, treatments_report, treatments, doctors_report), width = 16, height = 4)
        button2.place(x = 335, y = 230)

    if role == "Manager" or role == "Doctor":
        # assign assistant button
        button3 = tk.Button(text = "Assign assistant", command = lambda: AA.Assign_Assistant(root, username, role, users_data, patients, treatments_report, treatments, doctors_report), width = 16, height = 4)
        button3.place(x = 335, y = 320)

    if role == "Manager":
        # manage doctors button
        button4 = tk.Button(text = "Manage Doctors", command = lambda: MD.Manage_Doctors(root, username, role, users_data, patients, treatments_report, treatments, doctors_report), width = 16, height = 4)
        button4.place(x = 335, y = 410)

    if role == "Manager":
        # manage assistants button
        button5 = tk.Button(text = "Manage Assistants", command = lambda: MA.Manage_Assistants(root, username, role, users_data, patients, treatments_report, treatments, doctors_report), width = 16, height = 4)
        button5.place(x = 335, y = 500)

    if role == "Doctor":
        # recommand treatment button
        button6 = tk.Button(text = "Recommand treatment", command = lambda: MTD.Recommand_Treatment_Doctor(root, username, role, patients, users_data, treatments_report, treatments, doctors_report), width = 16, height = 4)
        button6.place(x = 335, y = 410)

    if role == "Assistant":
        # apply treatment button
        button7 = tk.Button(text = "Apply treatment", command = lambda: MTA.Apply_Treatment_Assistant(root, username, role, patients, users_data, treatments_report, treatments, doctors_report), width = 18, height = 4)
        button7.place(x = 335, y = 140)

    if role == "Assistant":
        # apply treatment button
        button8 = tk.Button(text = "View available treatments", command = lambda: VTA.View_Treatments_Assistant(root, username, role, patients, users_data, treatments_report, treatments, doctors_report), width = 18, height = 4)
        button8.place(x = 335, y = 230)

    root.mainloop()

def Sign_Out(root, users_data, patients, treatments_report, treatments, doctors_report):
    root.destroy()
    lg.login(users_data, patients, treatments_report, treatments, doctors_report)

def go_back_to_main_window(root, username, role, users_data, patients, treatments_report, treatments, doctors_report):
    root.destroy()
    main_window(username, role, users_data, patients, treatments_report, treatments, doctors_report)
