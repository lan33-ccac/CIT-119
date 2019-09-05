##################################################################
# Module: Calc_Falling_Distance.py
# Exercise:Ch5_Exercise_13.py
# Purpose: Calculates Falling Distance
# Last update: 10/15/18
# Author: Lisa Nydick
##################################################################

GRAVITY = 9.8
fatal_error = False # global error condition variable

def main():

    distance = 0 # in meters
    time = 0
    time = get_user_input()
    if fatal_error == False:
        distance = falling_distance(time)
        display_output(distance, time)



def get_user_input():
    t = 0
    while t == 0:
        try:
            t = int(input('Enter a valid falling time in seconds:'))
            if t <= 0:
                print('Time must be greater than 0.')
                t = 0
        except ValueError:
            print('Input must be a number')
            t = 0
        except err:
            print('Unexpected Error:', err, 'occurred. Ending program.')
            fatal_error = True
            t = 0
    return t


def falling_distance(t):
    d = 0
    d = 0.5 * (GRAVITY * (t**2))
    return d

def display_output(d, t):
    print('Object fell', format(d, '.2f'), 'meters', 'in', t, 'seconds.')

main()
