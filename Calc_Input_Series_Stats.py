##################################################################
# Module: Calc_Input_Series_Stats.py
# Exercise: Ch7_Exercise_4
# Purpose: Calculates stats on series of input numbers
# Last update: 10/24/2018
# Author: Lisa Nydick
##################################################################

#Global constants and variables declarations
MONTH_NAMES = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
MAX = 20



def main():
    #initialize local variables
    fatal_error = False
    series = []
    total = 0
    average = 0
    high = 0
    low = 0

    series, fatal_error = get_user_input(series)

    if fatal_error == False:
        total, average, high, low, fatal_error = compute_stats(series)

    if fatal_error == False:
        fatal_error = display_output(total, average, high, low)

    if fatal_error == True:
        print('Program terminated abnormally.')

def get_user_input(list):
    fatal_error = False
    current_num = 0
    i = 0

    for i in range(0, MAX, 1):
        current_num = 0
        index = str(i + 1)

        while current_num == 0:
            try:
                current_num = int(input('Enter series value ' + index + ': '))
                list.append(current_num)
            except ValueError:
                print('You did not enter a number.  Try again.')
                current_num = 0
                continue
            except Exception as err:
                print(err)
                print('Ending program.')
                fatal_error = True
                break


    return list, fatal_error

# function for computing stuff
def compute_stats (list):
    fatal_error = False
    total = 0
    average = 0
    high = 0
    low = 0

    for i in range(MAX):
        total += list[i]

    average = total/MAX
    high = max(list)
    low = min(list)

    return total, average, high, low, fatal_error



# function for displaying console output
def display_output(total, avg, high, low):
    fatal_error = False
    try:
        print('Total of the numbers in the series = ', total)
        print('Average = ', format(avg, '.2f'))
        print('High value = ', high)
        print('Low value = ', low)
    except Exception as err:
       print('Unexpected Error:', err, 'occurred. Ending program.')
       fatal_error = True

    return fatal_error


main()