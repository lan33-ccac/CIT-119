########################################################################
# Module: Employee_Mgmt_System.py
# Exercise: Ch10_Exercise_7
# Purpose: Employee Management System
# Last Update Date: 11/14/18
# Author: Lisa Nydick
########################################################################

import employee

# Global Constants
MENU_STR = 'EMPLOYEE MANAGEMENT MENU\n'
LOOKUP_STR = '1: Look up an employee record'
ADD_STR = '2: Add employee record'
CHANGE_STR = '3: Change employee record'
DELETE_STR = '4: Delete an employee record'
QUIT_STR = '5: Quit program'
CHOICE_STR = 'Enter the action you would like to perform: '
LOOKUP_INT = 0
ADD_INT = 1
CHANGE_INT = 3
DELETE_INT = 4
QUIT_INT = 5

def main():

    emp_name = ''
    emp_id = 0
    emp_dept = ''
    emp_title = ''
    employee_dict = {}
    emp_dict = {}
    employee_list = []
    user_choice = 0

    user_choice = display_menu()
    emp_dict = request_info_from_user(user_choice)



    empl = employee.Employee(emp_id, emp_name, emp_dept, emp_title)

    emp_dict = {'emp_id':47899, 'emp_name': 'Susan_Meyers', 'emp_dept': 'Accounting', 'emp_title': 'Vice President'}
    employee_list.append(emp_dict)
    emp_dict = {'emp_id':39119, 'emp_name': 'Mark Jones', 'emp_dept': 'IT', 'emp_title': 'Programmer'}
    employee_list.append(emp_dict)
    emp_dict = {'emp_id':81774, 'emp_name': 'Joy Rogers', 'emp_dept': 'Manufacturing', 'emp_title': 'Engineer'}
    employee_list.append(emp_dict)


    for i in range(len(employee_list)):
        employee_dict = employee_list[i]
        emp_id = employee_dict['emp_id']
        emp_name = employee_dict['emp_name']
        emp_dept = employee_dict['emp_dept']
        emp_title = employee_dict['emp_title']

        empl.set_id_number(emp_id)
        empl.set_name(emp_name)
        empl.set_department(emp_dept)
        empl.set_job_title(emp_title)

        print('Employee ID =', empl.get_id_number(emp_id))
        print('Employee Name=', empl.get_name(emp_name))
        print('Employee Department =', empl.get_department(emp_dept))
        print('Employee Title=', empl.get_job_title(emp_title))
        print('\n')
#######################################################
def display_menu():


    choice = 0


    while choice != QUIT_INT:
        print(MENU_STR)
        print(LOOKUP_STR)
        print(ADD_STR)
        print(CHANGE_STR)
        print(DELETE_STR)
        print(QUIT_STR)
        choice = int(input(CHOICE_STR))


    return choice
#######################################################
def request_info_from_user(menu_choice):

    empl_dict = {}

    return empl_dict
#######################################################
def lookup_employee(dict):

    empl_dict = {}

    return empl_dict

#######################################################
def add_employee(dict):

    empl_dict = {}

    return empl_dict
#######################################################
def change_employee(dict):

    empl_dict = {}

    return empl_dict

#######################################################
def delete_employee(dict):





#######################################################
main()
