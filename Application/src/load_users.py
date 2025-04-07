import os
import json

# read users from json
def load_users():
    if os.path.exists("./json/users/users.json"):
        try:
            with open("./json/users/users.json") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    else:
        return {}

# update users json
def update_users(users_data):
    if os.path.exists("./json/users/users.json"):
        try:
            with open("./json/users/users.json", 'w') as file:
                json.dump(users_data, file, indent=4)
        except json.JSONDecodeError:
            return {}

# read patients from json
def load_patients():
    if os.path.exists("./json/patients/patients.json"):
        try:
            with open("./json/patients/patients.json") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    else:
        return {}

# update patients json
def update_patients(users_data):
    if os.path.exists("./json/patients/patients.json"):
        try:
            with open("./json/patients/patients.json", 'w') as file:
                json.dump(users_data, file, indent=4)
        except json.JSONDecodeError:
            return {}

# load treatments report for every patient
def load_treatments():
    if os.path.exists("./json/patients_reports/treatments_report.json"):
        try:
            with open("./json/patients_reports/treatments_report.json") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    else:
        return {}

# update treatments report for every patient
def update_treatments(treatments_report):
    if os.path.exists("./json/patients_reports/treatments_report.json"):
        try:
            with open("./json/patients_reports/treatments_report.json", 'w') as file:
                json.dump(treatments_report, file, indent=4)
        except json.JSONDecodeError:
            return {}

# load doctors report for recommanded treatments
def load_doctors_report():
    if os.path.exists("./json/patients_reports/doctors_report.json"):
        try:
            with open("./json/patients_reports/doctors_report.json") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    else:
        return {}

# update doctors report for recommanded treatments
def update_doctors_report(doctors_report):
    if os.path.exists("./json/patients_reports/doctors_report.json"):
        try:
            with open("./json/patients_reports/doctors_report.json", 'w') as file:
                json.dump(doctors_report, file, indent=4)
        except json.JSONDecodeError:
            return {}
