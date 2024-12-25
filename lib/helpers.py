# lib/helpers.py
from models.hospital import Hospital
# from models.patient import Patient
# from models.patient import illnesses

def list_all_hospitals():
    hospitals = Hospital.get_all()
    for hospital in hospitals:
        print(f"{hospital.id}.Hospital: {hospital.name}| City: {hospital.city}")
    print("***Please choose of the following***")
    print("Type A to add a hospital. ")
    print("Type hospital's number for more info")
    print("Type b to go back")
    print("Type q to quit")
    choice = input("Enter your choice: ")
    if choice == "Q" or choice == "q":
        exit_program()
    elif choice =="B" or choice == "b":
        return "cd.."
    elif choice == "a" or choice =="A":
        create_hospital()
# def find_hospital_by_name():
#     name = input("Enter the hospital's name: ")
#     hospital = Hospital.find_by_name(name)
#     print(hospital) if hospital else print (f"Hospital {name} not found")

def create_hospital():
    name = input("Enter the hospital name:")
    city = input("Enter which city the hospital is in: ")
    try:
        Hospital.create(name,city)
    except Exception as exc:
        print("Error cannot be created", exc)


# def delete_hospital():
#     id = input("Enter the hospital id: ")
#     if hospital:= Hospital.find_by_id(id):
#         hospital.delete()
#         print(f"Succesfully deleted {hospital.name}")
            
#     else:
#         print(f"Deletion unsuccesful Id:{id} Not Found.")

# def search_hospitals_by_first_letter():
#     letter = input("Enter the first letter of the hospital name: ").lower()
#     filterd_hospitals = [hospital for hospital in Hospital.get_all() if hospital.name.lower().startswith(letter)]
#     if filterd_hospitals:
#         for hospital in filterd_hospitals:
#             print(hospital)
#     else:
#         print(f"{letter} Not Found")


# def list_all_patients():
#     patients = Patient.get_all()
#     for patient in patients:
#         print(patient)

# def find_patient_by_name():
#     name = input("Enter the patient's name: ")
#     patient = Patient.find_by_name(name)
#     print(patient) if patient else print(f"{name} Not Found.")


# def search_patients_by_first_letter():
#     letter = input("Enter The first letter of the patient's name: ")
#     filtered_patients = [patient for patient in Patient.get_all() if patient.name.lower().startswith(letter)]
#     if filtered_patients:
#         for patient in filtered_patients:
#             print(patient)
#     else:
#         print(f"{letter} Not Found")


# def create_patient():
#     name = input("Enter the patient's name: ")
#     age = input("Enter the patient's age: ")
#     for ill in illnesses:
#         print(ill)
#     illness = input("Chosse the Illness from above: ")
#     hospital_id = input("Enter the patient's hospital_id: ")
#     try:
#         patient = Patient.create(name,int(age),illness,int(hospital_id))
#         print(f"Succesfully created {patient}")
#     except Exception as exc:
#         print(f"unsuccesful could not create ",exc)

# def delete_patient():
#     id = input("Enter the patient's id you would like to delete: ")
#     if patient := Patient.find_by_id(id):
#         patient.delete()
#         print(f"Succesfully deleted {id}")
        
#     else:
#         print(f"{id} Not Found")

# def list_all_patients_with_same_illness():
#     for ill in illnesses:
#         print(ill)
#     illness = input("Enter The illness from above: ")
#     filtered_patients = [patient for patient in Patient.get_all()if illness == patient.illness ]
#     if filtered_patients:
#         for patient in filtered_patients:
#             print(patient)
#     else:
#         print(f"No one has same illness: {illness}")


def exit_program():
    print("Goodbye!")
    exit()
