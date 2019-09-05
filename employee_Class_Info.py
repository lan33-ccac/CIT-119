########################################################################
# Module: employee_Class_Info.py
# Exercise: Ch10_Exercise_4.py
# Purpose: Works with employee Class
# Last Update Date: 11/14/18
# Author: Lisa Nydick
########################################################################

import employee

def main():

    emp_name = ''
    emp_id = 0
    emp_dept = ''
    emp_title = ''
    employee_dict = {}
    emp_dict = {}
    employee_list = []

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


main()
