# lib/helpers.py
from models.hospital import Hospital
from models.patient import Patient

def list_all_hospitals():
    hospitals = Hospital.get_all()
    for hospital in hospitals:
        print(hospital)

def find_hospital_by_name():
    name = input("Enter the hospital's name: ")
    hospital = Hospital.find_by_name(name)
    print(hospital) if hospital else print (f"Hospital {name} not found")

def create_hospital():
    name = input("Enter name:")
    city = input("Enter city: ")
    try:
        hospital = Hospital.create(name,city)
        print(f"Successfully created:{hospital}")
    except Exception as exc:
        print("Error cannot be created", exc)


def delete_hospital():
    id = input("Enter the hospital id: ")
    try:
        if hospital:= Hospital.find_by_id(id):
            hospital.delete()
            print(f"Succesfully deleted {hospital.name}")
    except Exception as exc:
        print("Deletion unsuccesful",exc)

def search_hospitals_by_first_letter():
    letter = input("Enter the first letter of the hospital name: ")
    for hospital in Hospital.get_all():
        if hospital.name.startswith(letter):
            print(hospital)
    print(f"{letter} Not Found")
            

def list_all_patients_by_hospital_name():
    pass

def list_all_patients():
    pass

def find_patient_by_name():
    pass

def search_patients_by_first_letter():
    pass

def create_patient():
    pass

def delete_patient():
    pass

def list_all_patients_with_same_illness():
    pass

def exit_program():
    print("Goodbye!")
    exit()
