###########################################################################
# Module: Read_Rand_Nums_From_File.py
# Exercise: Ch6_Exercise_8
# Purpose: Random Number File Reader
# Author: Lisa Nydick
# Last Update: 10/10/2018
###########################################################################

def open_file(file_name):
    infile = open(file_name, 'r')
    return infile

def print_stats(rand_total, rand_count):
    print('A total of', rand_count, 'records were read.')
    print('The total value of the random numbers is:', rand_total)

def close_file(file):
    file.close

def main():
    rand_total = 0
    rand_count = 0
    input_line = ''
    random_num = 0
    infile = open_file('random.txt')

    for line in infile:

        input_line = line
        input_line = input_line.rstrip('\n')
        random_num = int(input_line)
        rand_count += 1
        rand_total += random_num

    print_stats(rand_total, rand_count)
    close_file(infile)

main()


