########################################################################
# Module: Get_ShiftSupervisor_Info.py
# Exercise: Ch11_Exercise_2
# Purpose: Employee and ShiftSupervisor Exercise #2 in Ch 11
# Last Update Date: 11/30/18
# Author: Lisa Nydick
########################################################################

from employee import ShiftSupervisor

def main():

    worker_name = ''
    worker_number = 0
    annual_salary = 0
    bonus = 0

    worker_name, worker_number, annual_salary, bonus = get_user_input()
    worker = ShiftSupervisor(worker_name, worker_number, annual_salary, bonus)
    print_worker(worker)


def get_user_input():

    worker_name = ''
    worker_number = 0
    annual_salary = 0
    bonus = 0

    worker_name = input('Enter the name of the Shift Supervisor: ')
    worker_number = int(input('Enter the employee number: '))
    annual_salary = float(input('Enter the annual pay: '))
    bonus = float(input('Enter the production bonus: '))

    return worker_name, worker_number, annual_salary, bonus



def print_worker(worker):
    print('Shift Supervisor Name:', worker.get_name())
    print('Employee Number:', worker.get_number())
    print('Annual Salary:', worker.get_annual_salary())
    print('Production Bonus:', worker.get_bonus())


main()
