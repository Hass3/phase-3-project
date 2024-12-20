# lib/cli.py

from helpers import (
    exit_program,
    list_all_hospitals,
    find_hospital_by_name,
    create_hospital,
    delete_hospital,
    search_hospitals_by_first_letter,
    list_all_patients,
    find_patient_by_name,
    search_patients_by_first_letter,
    create_patient,
    delete_patient,
    list_all_patients_with_same_illness
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_hospitals()
        elif choice =="2":
            find_hospital_by_name()
        elif choice == "3":
            create_hospital()
        elif choice =="4":
            delete_hospital()
        elif choice == "5":
            search_hospitals_by_first_letter()
        elif choice == "6":
            list_all_patients()
        elif choice == '7':
            find_patient_by_name()
        elif choice == "8":
            search_patients_by_first_letter()
        elif choice == "9":
            create_patient()
        elif choice == "10":
            delete_patient()
        elif choice == "11":
            list_all_patients_with_same_illness()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. list all hospitals")
    print("2. Find hospital by name")
    print("3. Create hospital")
    print("4. Delete hospital")
    print("5. Search for hospitals by entering the first letter of the name")
    print("6 List all patients")
    print("7. Find patient by name ")
    print("8. Search for patients by entering the first letter of their name")
    print("9. Create patient")
    print("10: Delete patient")
    print("11. List all patients with the same illness")

if __name__ == "__main__":
    main()
