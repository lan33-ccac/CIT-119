##################################################################
# Module: Simulate_Magic_8_Ball.py
# Exercise:Ch7_Exercise13
# Purpose:Simulate Magic 8 Ball
# Last update:06/06/19
# Author: Lisa Nydick
##################################################################

#Global constants and variables declarations
FILE_NAME = "magic_8_sayings.txt"
MIN_RAND = 0
MAX_RAND = 11
fatal_error = False # global error condition variable

def main():
    #initialize local variables
    list_of_sayings = []
    question = ""
    done = 'N'
    random_int = 0
    magic_8_response = ""
    list_of_sayings = read_file(FILE_NAME)
    print(list_of_sayings)


    while done != 'Y':
        question = input('Enter a question: ')
        if question != "":
            random_int = get_random_int(MIN_RAND, MAX_RAND)
            print(random_int)
            magic_8_response = get_magic_8_response(list_of_sayings, random_int)
            print(magic_8_response)
        else:
            print("You didn't enter a question")


        done = input("End program?  'Y' or 'N': ")


# Function for reading and displaying the contents of a file
def read_file(filename):
    sayings_list = []
    saying = ""
    # Open the file containing the magic 8 ball text
    infile = open(filename, 'r')

    saying = infile.readline()
    while saying != "":
        saying = saying.rstrip('\n')
        sayings_list.append(saying)
        saying = infile.readline()

    infile.close()

    #print(sayings_list)

    return sayings_list

# Function takes a min and max value and generates a random number in that range.
# Returns the randomly generated integer
def get_random_int(min, max):
    random_int = 0
    # import random number library
    from random import randint
    random_int = randint(min, max)
    return random_int

def get_magic_8_response(response_list, random_num):
    return response_list[random_num]


main()
