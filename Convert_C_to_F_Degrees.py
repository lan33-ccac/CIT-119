###########################################################################
# Module: Convert_C_to_F_Degrees.py
# Exercise:Ch4_Exercise_6
# Purpose: Converts Celcius to Fahrenheit Table
# Author: Lisa Nydick
# Last Update: 10/03/2018
###########################################################################

MAX = 20

print('Celcius\t\tFahrenheit')
print('_________________________')

for c in range(0, MAX + 1):
    f = 9 / 5 * c + 32
    print(format(c, '2.0f'), '\t', format(f, '14.2f'))