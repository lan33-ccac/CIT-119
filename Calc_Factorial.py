###########################################################################
# Module: Calc_Factorial.py
# Exercise: Ch4_Exercise_12
# Purpose: Calculate Factorial
# Author: Lisa Nydick
# Last Update: 10/03/2018
###########################################################################

total = 1
start = 1
end = 1
step = 1

value = input('Enter a non-negative number')
while len(value) == 0 or value.isalpha():
    value = input('Input must be a non-negative number')

value = int(value)
while value < 0:
    value = int(input('Input must be a non-negative number'))
               
end = value + 1

for i in range(start, end, step):
    total = total * i

print(value, '! = ', total)