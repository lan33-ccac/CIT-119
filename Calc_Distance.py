###########################################################################
# Module: Calc_Distance.py
# Exercise: Ch4_Exercise_4
# Purpose: Calculates distance traveled
# Author: Lisa Nydick
# Last Update: 10/03/2018
###########################################################################

speed = int(input('What is the speed of the vehicle in mph?'))
hours = int(input('How many hours has it traveled?'))

print('Hour\tDistance Traveled')
print('_________________________')

for h in range(1, hours + 1):
    distance = h * speed 
    print(h, '\t', format(distance, '8,d'))