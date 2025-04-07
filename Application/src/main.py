import load_users as ls
import load_treatments as lt
import login as lg

if __name__ == '__main__':
    # get users data from json
    users_data = ls.load_users()
    # get patients data from json
    patients = ls.load_patients()
    # get treatments report for patients from json
    treatments_report = ls.load_treatments()
    # get doctors report for patients from json
    doctors_report = ls.load_doctors_report()
    # get available treatments from json
    treatments = lt.get_treatments()

    # login component
    lg.login(users_data, patients, treatments_report, treatments, doctors_report)
