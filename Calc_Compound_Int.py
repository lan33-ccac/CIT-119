###########################################################################
# Module: Calc_Compound_Int.py
# Exercise: Ch 2 Exercise 14
# Purpose: Calculates compound interest
# Author: Lisa Nydick
# Last Update: 09/28/2018
###########################################################################

principal = int(input('Enter amount of principal deposited to account:'))
interest = float(input('Enter annual interest rate in %:')) / 100
compound_count = int(input('Enter number of times interest is compounded annually:'))
accrual_years = int(input('Enter number of years account will accrue interest:'))

# Formula = Amount = principal * (1 + interest / compound_count) ** (compound_count * accrual_years)
amount = principal * (1 + interest / compound_count) ** (compound_count * accrual_years)
print('Your account will be worth $', format(amount, ',.2f'), 'in', accrual_years, 'years.')
