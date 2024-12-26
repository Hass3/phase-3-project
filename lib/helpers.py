# lib/helpers.py
from models.hospital import Hospital
from models.patient import Patient

def list_all_hospitals():
    hospitals = Hospital.get_all()
    print("===================================================================")
    print("**ALL HOSPITALS**")
    for i, hospital in enumerate(hospitals,start=1):
        print(f"{i}.name of hospital: {hospital.name}, City: {hospital.city}")
    print("***Please choose of the following***")
    print("Type hospital's number for more info")
    print("or")
    print("Type a to add a hospital. ")
    print("Type b to go back")
    print("Type q to quit")
    print("===================================================================")
    choice = input("Enter your choice: ")
    if choice == "Q" or choice == "q":
        exit_program()
    elif choice =="B" or choice == "b":
        return "cd.."
    elif choice == "a" or choice =="A":
        create_hospital()
    elif choice.isdigit() and int(choice) in range(1,len(hospitals)+1):
        list_all_patients(hospitals[int(choice)-1])
    else:
        print("Incorrect choice please try again")



def list_all_patients(h):
    print("===================================================================")
    print(f"***ALL Patients of the {h.name} Hospital***")
    patients = Hospital.patients(h)
    for i,patient in enumerate(patients,start=1):
        print(f"{i}.Name: {patient.name}")
    print("Type the patient's number for more info")
    print ("or")
    print("Type a to add a patient")
    print("Type b to go back")
    print("Type m for main menu")
    print("Type q to quit")
    print("Type d to delete hospital ")
    print("===================================================================")
    choice = input("Enter your choice: ")
    
    if choice == "b" or choice == "B":
        list_all_hospitals()       
    elif choice == "q" or choice == "Q":
        exit()
    elif choice =="m" or choice =="M":
        return 
    elif choice == "d" or choice == "D":
        Hospital.delete(h)
        for p in patients:
            p.delete()
        list_all_hospitals()
    elif choice == "a" or choice =="A":
        create_patient(h)
    elif choice.isdigit() and int(choice) in range(1,len(patients)+1):
        chosen_patient(patients[int(choice)-1])
    else:
        print("Incorrect choice please try again")
    

def create_patient(h):
    name = input("Enter the patient's name: ")
    age = input("Enter the patient's age: ")
    illness = input("Enter the patient's illness: ")
    try:
        Patient.create(name,int(age),illness,h.id)
        list_all_patients(h)
    except Exception as exc:
        print("***The patient could not be added try again***", exc)

def create_hospital():
    name = input("Enter the hospital name:")
    city = input("Enter which city the hospital is in: ")

    try:
        Hospital.create(name,city)
        list_all_hospitals()
    except Exception as exc:
        print("*******The hospital cannot be created please try again********.",exc)

def chosen_patient(p):
    print("---------------------------------------")
    print(f"****{p.name}'s Information****")
    print(f"Age: {p.age}")
    print(f"illness:{p.illness}")
    print("Type u or U to update patient")
    print("or")
    print("Type r to remove the patient")
    print("Type b to go back")
    print("Type m for main menu")
    print("Type q to quit")
    print("---------------------------------------")
    choice = input("Enter your choice: ")
    if choice == "u" or choice == "U":
        update_patient(p)
    elif choice == "b" or choice == "B":
        go_back_patients(p)
    elif choice == "u" or choice == "U":
        update_patient(p)
    # elif choice =='r' or choice == "R":
    #     Patient.delete(p)                     ## work on this 
    #     go_back_patients(p)
    elif choice == "q" or choice == "Q":
        exit()
    elif choice =="m" or choice =="M":
        return 
    else:
        print("Incorrect choice please try again")

def update_patient(p):
    try:
        name = input("Enter new name: ")
        p.name = name
        age = input("Enter New Age: ")
        p.age = int(age)
        illness = input("Enter New illness: ")
        p.illness = illness
        p.update()
        chosen_patient(p)
    except Exception as exc:
        print(f"****could not update {p.name} please try again****",exc)

def go_back_patients(p):
    for hospital in Hospital.get_all():
        if p.hospital_id == hospital.id:
            list_all_patients(hospital)




def exit_program():
    print("Goodbye!")
    exit()
