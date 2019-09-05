###########################################################################
# Module: Write_Random_Nums_to_File.py
# Exercise: Ch6_Exercise_7
# Purpose: Random Number File Writer
# Author: Lisa Nydick
# Last Update: 10/10/2018
###########################################################################


def get_input():
    num_random_numbers_to_write = int(input('Enter number of random numbers to write: '))
    while num_random_numbers_to_write < 1:
        print('Number must be 1 or more.')
        num_random_numbers_to_write = int(input('Enter a valid number of random numbers to write'))
    return num_random_numbers_to_write

def get_random():
    from random import randrange
    rand_num = randrange(1, 500)
    return(rand_num)

def write_file(file, rand_num):
    file.write(str(rand_num) + '\n')

def close_file(file):
    print('Random numbers written.')
    file.close

def main():
    num_values_to_write = get_input()
    #path = 'C:\Users\lnydi\Documents\CIT-119\PythonApplication1'
    outfile = open('random.txt', 'w')
   
    for i in range(1, num_values_to_write + 1, 1):
        random_num = get_random()
        write_file(outfile, random_num)
    close_file(outfile)

main()