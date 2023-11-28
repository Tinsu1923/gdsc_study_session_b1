'''Task: Student Database

Create a simple student database program using Python dictionaries and basic data types. The program should be able to perform the following actions:

Add Student: Allow the user to add a new student to the database. Collect information such as name, age, grade, and any other relevant details.

View Student: Allow the user to view the details of a specific student by entering the student's name.

List All Students: Display a list of all students in the database with their basic information.

Update Student Information: Allow the user to update the information of a specific student, such as changing their grade or age.

Delete Student: Allow the user to delete a student from the database based on their name.
"""
'''
from collections import defaultdict
studentInfo = defaultdict(list)
def addStudent():
    name = input("Enter the student name: ")
    age = input("Enter the student age: ")
    grade = input("Enter the student grade: ")
    dept = input("Enter the student department: ")
    studentInfo[name] = [age,grade,dept] 
    print("Student information successfully added.")
    return
def viewStudent():
    name = input("Enter the student name: ")
    if name in studentInfo:
        print(studentInfo[name])   
    else:
        print("No such student exists. Try again.")
    return
def updateStudent():
    name_to_update = input("Enter the name of the student u wanna update: ").lower()
    for name in studentInfo:
        if name.lower() == name_to_update:
            value = int(input("What do u wanna update? Enter 0 for age, 1 for grade and 2 for department: "))
            if value == 0:
                age = input("Enter the new age: ")
                studentInfo[name][0] = age
                print("Successfully updated!")
            elif value == 1:
                grade = input("Enter the new grade: ")
                studentInfo[name][1] = grade
                print("Successfully updated!")
            elif value == 2:
                dept = input("Enter the new department ")
                studentInfo[name][2] = dept
                print("Successfully updated!")
            else:
                print("Invalid input. ")
        else:
            print("No such key exists.")
    return
def deleteStudent():
    name_to_delete = input("Enter the student name to delete.")
    if name_to_delete in studentInfo:
        del(studentInfo[name_to_delete])
        print("Student info successfully deleted.")
    return         
def main():
    print("Welcome to the simple student database program! ")
    flag = True
    while(flag):
        print("Enter your choice: \n 1. Add a student to the database \n 2. View the student's details \n 3. Update student information \n 4. Delete a student from the database. \n Enter any other number to exit the program." )
        num = int(input())
        if num == 1:
            addStudent()
        elif num == 2:
            viewStudent()
        elif num == 3:
            updateStudent()
        elif num == 4:
            deleteStudent()
        else:
            print("Exiting the program.")
            flag = False
main()

