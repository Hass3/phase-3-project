Health:Project

For this project I created a command line interface based on a one to many relationship.

## Patient.py
In the patient.py file there is a class that serves as the many of the one to many relationship.
For this class. I created through best practices Object-Relational-mapping functionalty that allow me
to create,delete,find my database using python.Also creaing a table for my database

## Hospital.py
In the hospital.py file the class serves as the One to the one to many relationship. 
This class also uses Object-Relational-mapping functionalty that allows to create, delete and find my database 
using python. Also creating A table for my database 

## cli.py
My Command Line Interface file when runned, Prompts the following commands that the user will be able to enter.
I imported the Helper funtions from Helpers.py to fulfill those desired commands.When this file is runned the printed commands
appear and whatever the user enters 0-11 runs the command.

## Helpers.py
For this file, I created a few helper functions to accomplish the desired commands in the CLI.
Imported is the Patient and Hospital classes which allow me to make these speical functions like allowing the user to
create, find, delete.This makes my appliction user friendly not showing the backend and allows easy implementation of the database
through the command line interface.  

## A few Helper functions created
1.def search_patients_by_first_letter(). This function allows the user enter the first letter of the patient's name. 
Also returns all the patients with that same first letter. This functionalty is also case insensive and allows the user to enter a lower or
upper case letter and returns the same result.

2.def list_all_patients_with_same_illness() For this function I imported the illness list from my patients.py file. 
This function prompts the user to enter one of the above ilness from my illnesses list. When entered A list of all the patients
with the same illness appears.

