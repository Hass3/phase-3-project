# lib/cli.py

from helpers import (
    exit_program,
    hospitals_helper
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            hospitals_helper()
        elif choice == "2":
            exit_program()

def menu():
    print("_____Main Menu____")
    print("****Welcome Back! Please select an option****:")
    print("1. Show All Hospitals ")
    print("2. Quit")

if __name__ == "__main__":
    main()
