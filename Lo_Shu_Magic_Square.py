######################################################################################################
# Module: Lo_Shu_Magic_Square.py
# Exercise: Ch7_Exercise_11
# Purpose: Checks whether numbers input by user form a Lo Shu Magic Square
# Last update: 10/27/2018
# Author: Lisa Nydick
######################################################################################################

#Global constants and variables declarations
MAX_ROWS = 3
MAX_COLS = 3


######################################################################################################
def main():
    #initialize local variables
    fatal_error = False
    input_square = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    magic_square = False    # Boolean var indicates whether input values meet criteria for Lo Shu Magic Square

    # Call function to receive user values and store them in a 2-dimensional list
    input_square, fatal_error = get_user_input(input_square)

    # If a fatal error did not occur in the previous function
    # Call a function to test the values of rows and columns in the square
    # The returned value of the magic_square variable indicates whether the values in the square met the magic square criteria
    if fatal_error == False:
       magic_square, fatal_error = compute_square(input_square)

    # If a fatal error did not occur in the previous function
    # Call a function to display the magic_square outcome
    if fatal_error == False:
        fatal_error = display_output(magic_square)

    # If a fatal error occurred somewhere along the way, indicate that the program did not finish running
    if fatal_error == True:
        print('Program terminated abnormally.')

######################################################################################################
# function fills a 2-dimensional list with values entered by a user
def get_user_input(square):
    fatal_error = False
    current_num = 0
    r = 0
    c = 0
    used_nums = []  # variable for storing values user has already entered

    # Nested loop for receiving input
    for r in range(MAX_ROWS):
        current_num = 0
        row_index = str(r + 1)  # used to display row number for user

        for c in range(MAX_COLS):
            col_index = str(c + 1)  # used to display col number for user
            current_num = 0

            # Keep prompting for input value until a valid number has been entered
            while current_num == 0:
                try:
                    current_num = int(input('Enter row ' + row_index + ', column ' + col_index + ': '))

                    # Make sure number hasn't been entered already by checking for it's presence in the used_nums list
                    if current_num in used_nums:
                        print('You already used that number in the square.  Try another.')
                        current_num = 0
                    # Check that number entered is in a valid range
                    elif current_num < 1 or current_num > 9:
                        print('Number must be between 1 and 9.  Try again.')
                        current_num = 0
                    else:
                        # insert user value into current cell, and add it to the used number list
                        square[r][c] = current_num
                        used_nums.append(current_num)
                except ValueError:
                    print('You did not enter a number.  Try again.')
                    current_num = 0
                    continue
                except Exception as err:
                    print(err)
                    print('Ending program.')
                    fatal_error = True
                    break
    return square, fatal_error

######################################################################################################
# function for computing stuff
def compute_square (square):
    fatal_error = False
    magic_square = True
    row_total = 0
    col_total = 0
    r = 0
    c = 0

# Check row totoals
    try:
        for r in range(MAX_ROWS):
            if magic_square == True:
                for c in range(MAX_COLS):
                    row_total += square[r][c]
                if row_total != 15:
                    magic_square = False
                    break
                else:
                    row_total = 0
    except Exception as err:
        print(err)
        print('Ending program.')
        fatal_error = True

    if fatal_error == False:
        # Check column totals
        try:
            for c in range(MAX_COLS):
                if magic_square == True:
                    for r in range(MAX_ROWS):
                        col_total += square[r][c]
                    if col_total != 15:
                        magic_square = False
                    break
                else:
                    col_total = 0
        except Exception as err:
            print(err)
            print('Ending program.')
            fatal_error = True

    return magic_square, fatal_error


######################################################################################################
# function for displaying console output
def display_output(magic_square):
    fatal_error = False
    try:
        if magic_square == False:
            print('This is not a Lo Shu Magic Square.')
        else:
            print('This is a Lo Shu Magic Square.')
    except Exception as err:
       print('Unexpected Error:', err, 'occurred. Ending program.')
       fatal_error = True

    return fatal_error

######################################################################################################
main()
