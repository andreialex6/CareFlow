import json
import tkinter as tk
from tkinter import messagebox

def Download_Patients_Report():
    file_path = './json/patients_reports/treatments_report.json'

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        with open('./../Downloaded_Reports/Patients_Reports.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
        
        tk.messagebox.showinfo("Succes", "Report was successfully downloaded! You can see it in Downloaded_Reports folder.")

    except FileNotFoundError:
        tk.messagebox.showinfo("Erorr", "No report found to download!")

def Download_Doctors_Report():
    file_path = './json/patients_reports/doctors_report.json'

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        with open('./../Downloaded_Reports/Doctors_Reports.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
        
        tk.messagebox.showinfo("Succes", "Report was successfully downloaded! You can see it in Downloaded_Reports folder.")

    except FileNotFoundError:
        tk.messagebox.showinfo("Erorr", "No report found to download!")
