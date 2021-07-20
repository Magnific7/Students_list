#!/usr/bin/python
import re

# Declaring files as strings to iterate them easily  

student_file = 'students.txt'
final_student_file = 'final_students.txt'

student_id = input('please enter a student id : ')


# function to verify if the id of a student exists in the students.txt file

def id_verification(student_id,student_file):
    for line in open(student_file, 'r'):
        id = line.split(',')[0].split(':')[1]
        if id == student_id:
            return True

#function to update the password to the final_students.txt file 
def update_password(student_id, password):
    
    # checking if student already has a password
    if id_verification(student_id,final_student_file) == True:
        print('Student with ID' + student_id + ' already has a password')
    
    # else setting the whole line of the student credentials with password  
    else:
        initial_students = open(student_file, 'r')
        for line in initial_students:
            id = line.split(',')[0].split(':')[1]
            if id == student_id:
                firstname = line.split(',')[1].split(':')[1]
                lastname = line.split(',')[2].split(':')[1].strip()
                final_students = open(final_student_file, 'a')
                L = ['id:'+ id +',firstname:'+firstname + ',lastname:' + lastname + ',password:' + password + '\n']
                final_students.writelines(L)
                print('successful ')

# verification of strong password
def password_verification(password):
    
    special_character =['$', '@', '#', '%', '*', '^', '&', '(', ')', '_']
    reserved_character = ['!', '+', '=']
    val = True
        
    if len(password) < 8:
        print('length should be at least 8')
        val = False
        
    if any(char in reserved_character for char in password):
        print('Password can not have special characters such as +,! and =')
        val = False
        
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
        
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
        
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False
        
    if not any(char in special_character for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        print('Yay password updated')
        update_password(student_id,password)
        return val

# set number of trials a user can enter a password
def set_password_trials():

    password_trial = input("Enter a strong password !!: ")
    if not password_verification(password_trial):
        password_trial = input("Enter a strong password , you have one attempt left: ")
        if not password_verification(password_trial):
            password_trial = input("Enter a strong password , this is your last trial: ")
            if not password_verification(password_trial):
                print(';)You have exceeded the number of attempts!!')


# renndering functions in order 
if id_verification(student_id,student_file):
    set_password_trials()

else:
    print("Please a enter a valid student id")