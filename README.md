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
I imported the Helper funtion hospitals_helper from Helpers.py. The main menu of my cli shows a welcome message plus 
a choice to choose of the following show all hospitals and quit. 
## Helpers.py
For my Helpers.py file i created a few functions to help make this CLI very user friendly.A few of these helper functions 
implement features like fetching all the hospitals or patients.Allow uses to go back or go to the main menu. Allow the user to 
update, add, or delete a hospital or patient. 


## A few Helper functions created
1. ### def hospitals_helper(): 

This function prints out all the hospitals in a numbered order. The user is able to add a hospital,
go back, quit, or type the hospital's number for more information. If the user types the desired hospital's number then.
All the patients for that hosptial shows up using the patients_helper() function.

2. ### def patients_helper(): 

For this function a few things are impleted simmarly to the function explained above.
One of which being when the hospital number is typed this function prints out all the patients for that specifc hospital. 
in a numbered list This function allows the user to delete the hospital, add a new patient, go back,main menu, or quit the progran. Also allows
the user to type in the patients number for more info. 

3. ### def chosen_patient(): 

In this function, I allowed the user to do of the following. Update, delete the patient, go back, main menu, 
and quit the program. All these functions and this one prints out prompts and implements features that helps the command line interface 
become very user friendly. 
