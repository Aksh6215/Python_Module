'''
Hospital Appointment System

Objective:
Build a Hospital Appointment System where patients can:
✔Register as a new patient
✔Book an appointment with a doctor
✔View available doctors
✔Check appointment history

Requirements:
-> Use a list of tuples to store doctor details (Doctor Name, Specialization).
-> Use a dictionary to manage patient appointments.
-> Implement functions for appointment booking, checking available doctors, and viewing patient history.
-> Use sets to track unique patient IDs.

'''
'''
# Hospital Appointment System
DoctorsDetail = [
    ("1", "Dr. Mehta", "Cardiologist"),
    ("2", "Dr. Sharma", "Dentist"),
    ("3", "Dr. Kohli", "Neurologist")
]

PatientDetails = {}
Patient_id = set()
Appointment_dict = {}

def Patient_Registration():
    pat_id = input("Enter patient id: ").strip()
    pat_name = input("Enter patient name: ").strip().lower()
    
    if pat_id in Patient_id:
        print("Patient ID already exists.")
    else:
        PatientDetails[pat_id] = [pat_name]
        Patient_id.add(pat_id)
        print("Patient registered successfully.")
        print(PatientDetails)

def BookAppointment():
    Doctor_id = input("Enter the doctor id: ").strip()
    if Doctor_id not in DoctorsDetail:
        print("Patient ID does not exist.")
        return

    for i in DoctorsDetail:
        if Doctor_id == i[0]:
            Appointment_dict[Doctor_id] = PatientDetails[Doctor_id]
            print("Appointment booked successfully.")
            print(Appointment_dict)
            return
    print("Invalid Doctor ID.")

def AvailableDoctors():
    for i in DoctorsDetail:
        print(i)

def AppointmentHistory():
    if Appointment_dict == {}:
        print("No appointments booked yet.")
    for i, j in Appointment_dict.items():
        print(i, j)

print("\n----- Hospital Appointment System -----")
while True:
    choice = int(input("\n 1. Patient Registration \n 2. Book Appointment \n 3. Available Doctors \n 4. Appointment History \n 5. Exit \nEnter your choice: "))

    if choice == 1:
        Patient_Registration()
    elif choice == 2:
        BookAppointment()
    elif choice == 3:
        AvailableDoctors()
    elif choice == 4:
        AppointmentHistory()
    elif choice == 5:
        print("Exiting...")
        print("Thank you for using the Hospital Appointment System.")
        break
    else:
        print("Invalid choice! try again.")
'''
# completed

"""
1) Hospital Appointment System
Objective:
Build a Hospital Appointment System where patients can:
✅ Register as a new patient
✅ Book an appointment with a doctor
✅ View available doctors
✅ Check appointment history
Requirements:
 Use a list of tuples to store doctor details (Doctor Name, Specialization).
 Use a dictionary to manage patient appointments.
 Implement functions for appointment booking, checking available doctors, and viewing
patient history.
 Use sets to track unique patient IDs.
"""
import datetime

DoctorsDetail = [("Anis Naroo", "Neurologist"), ("Rizwaan Naroo", "Heart Specialist"), ("Manish Sanyee", "Dentists"), ("Mansi Sharma", "cardiologist")]

appointments = {}
id_list = set()
patient_history = {}

def Booked_Appointment():
    doc_name = input("Enter doctor name:")
    count = 0
    if user_id in appointments:
        print(f"You have appointment with {appointments[user_id][0]}")
    else:
        for i in DoctorsDetail:
            if doc_name.lower() == i[0].lower():
                appointments[user_id] = i
                print("Appointment Booked")
                DoctorsDetail.pop(count)
                dt = datetime.datetime.now()
                patient_history[dt] = user_id, user_name, i
            count += 1

def available_doc():
    if len(DoctorsDetail) != 0:
        for i in DoctorsDetail:
            print(i[0]+" "+i[1])
    else:
        print("No available doctors.")

def pat_history():
     for x,y in patient_history.items():
        if y[0] == user_id:
            print(x, y)

while True:
    user_id = input("Enter ID: ")
    user_name = input("Enter user name: ")
    if user_id not in id_list:
        id_list.add(user_id)
        print("User is successfully registered.")
    else:
        print("Patient already registered.")
    
    while True:

        request = int(input("Enter your request: \n 1. Appointment booking\n 2. Available doctors\n 3. Patient history\n 4. Exit\n"))
        if request == 1:
            available_doc()
            Booked_Appointment()
        elif request == 2:
            available_doc()
        elif request == 3:
            pat_history()
        elif request == 4:
            break


# def end_appointment():
#     if user_id in patient_appointments.keys():
#         doctor_details.append(patient_appointments[user_id])
#         del patient_appointments[user_id]
#         print("Appointment Ended.")
#     else:
#         print("No appointment available.")