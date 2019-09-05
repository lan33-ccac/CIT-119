########################################################################
# Module: Get_ProductionWorker_Info.py
# Exercise: Ch11_Exercise_1.py
# Purpose: Employee and ProductionWorker Exercise #1 in Ch 11
# Last Update Date: 11/28/18
# Author: Lisa Nydick
########################################################################

from employee import ProductionWorker

def main():

    worker_name = ''
    worker_number = 0
    shift_number = 0
    hourly_rate = 0

    worker_name, worker_number, shift_number, hourly_rate = get_user_input()
    worker = ProductionWorker(worker_name, worker_number, shift_number, hourly_rate)
    print_worker(worker)


def get_user_input():

    worker_name = ''
    worker_number = 0
    shift_number = 0
    hourly_rate = 0

    worker_name = input('Enter the worker name: ')
    worker_number = int(input('Enter the worker number: '))
    while shift_number != 1 and shift_number != 2:
        shift_number = int(input('Enter the shift number.  1= Day, 2=Night: '))
    hourly_rate = float(input('Enter the hourly pay rate: '))

    return worker_name, worker_number, shift_number, hourly_rate



def print_worker(worker):
    print('Worker Name:', worker.get_name())
    print('Worker Number:', worker.get_number())
    print('Worker Shift_Number:', worker.get_shift_number())
    print('Hourly Rate:', worker.get_hourly_rate())


main()
