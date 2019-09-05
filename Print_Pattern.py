############################################
# Module: Print_Pattern.py
# Exercise: Ch4_Exercise_14
# Purpose: Prints a pattern
# Author: Lisa Nydick
# Last Update: 10/17/2018
############################################

MAX = 7

for r in range(MAX, 0, -1):
    #print('r=', r)
    for c in range(r):
        #print('c=', c)
        print('*', end = '')
    print()