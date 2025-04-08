# CareFlow

CareFlow is an application designed to handle main activities in a hospital.
It is implemented using Tkinter Gui from Python, having a graphical
interface for the application.

How to run the application
-
* You have to use 'make' command in the 'Application' folder to
turn on the API. The downloaded reports can be found in 'Downloaded_Reports'
folder. Users' credentials can be accessed from json/users/users.json.
After you run the application, you have to login with a username and a password.

Implementation description
-
* The application is used to handle main activities in a hospital,
involving 3 different roles, with different types of accounts:
Manager, Doctor and Assistant. These accounts with their credentials
and roles are stored in users.json, where the application will search
for correct credentials at the login stage. Manager's accounts can't be
created inside the application, being only possible to insert them directly
into json file. Accounts for doctors are created in application by Managers,
and Assistants are also created by Managers and Doctors. There is also the
possibility to remove a Doctor or Assistant account and also to update them.
Patients are introduced manually in application by managers and doctors, inluding
their problems. Patients' data are stored in patients.json.
* Available treatments are introduced by Doctors and Managers. Doctors can recommand
treatments for patients, but treatments have to be available(tratments have to be
in stock).
* Every patient will be assigned to an Assistant by Doctors and Managers and every
patient can have multiple Assistants. An Assistant can only see the patients that have
been assigned to them and apply treatments only to them.
* An Assistant can apply treatment only to patients that have a recommanded treatment
by a doctor and can only apply a treatment that had been recommanded.
* Managers have also the possibilty to download a report with all Doctors and the
treatments recommanded by them, finding the report in Downloaded_Reports folder,
using json format.
* Managers and Doctors can download a report with all Patients and the
treatments applied by Assistants, finding the report in Downloaded_Reports folder,
using json format.
    I used json files to store data about patients and available treatments.
    Data is persistent between successive restarts of the application, data being
read from jsons every time the application is opened. Data is also updated in jsons
every time a new item is added or updated in application.
