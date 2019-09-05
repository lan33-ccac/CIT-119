########################################################################
# Filename: employee.py
# Purpose: Class definition for Employee Object Used in Ch 11 Exercise
# Last Update Date: 11/29/18
# Author: Lisa Nydick
########################################################################
class Employee:

    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = int(number)

class ProductionWorker(Employee):

    def __init__(self, name, number, shift_number, hourly_rate):

        Employee.__init__(self, name, number)
        self.__shift_number =shift_number
        self.__hourly_rate = hourly_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_rate(self):
        return self.__hourly_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = int(shift_number)


    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = float(hourly_rate)

class ShiftSupervisor(Employee):

    def __init__(self, name, number, annual_salary, bonus):

        Employee.__init__(self, name, number)
        self.__annual_salary = annual_salary
        self.__bonus = bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_bonus(self):
        return self.__bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = float(annual_salary)

    def set_bonus(self, bonus):
        self.__bonus = float(bonus)
