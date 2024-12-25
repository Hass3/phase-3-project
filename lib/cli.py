# lib/cli.py

from helpers import (
    exit_program,
    list_all_hospitals
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            list_all_hospitals()
        elif choice == "2":
            exit_program()

def menu():
    print("****Welcome Back! Please select an option****:")
    print("1. Show All Hospitals ")
    print("2. Quit")

if __name__ == "__main__":
    main()
