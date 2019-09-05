##################################################################
# Module: Powerball.py
# Exercise: Ch8_Exercise_13.py
# Purpose: Computes frequency of numbers that appear in powerball file
# Last update: 10/31/18
# Author: Lisa Nydick
##################################################################

#Global constants and variables declarations
FILENAME= 'pbnumbers.txt'
NUMS_DRAWN = 5
MAX_NUM = 69
MAX_PB_NUM = 26
RANGE = 10   # for min and max functions
number_list = []
powerball_list = []
num_freq_list = []
pb_freq_list = []
most_freq_num_list = []
most_freq_pb_list = []
least_freq_num_list = []
least_freq_pb_list = []
most_overdue_num_list = []
most_overdue_pb_list = []


print('############## MAIN START #####################################')
def main():
    #initialize local variables
    fatal_error = False


    outfile = open('pbdebug.txt', 'w')

    if fatal_error == False:
        # No fatal error has occurred so keep processing stuff
        all_draws_list = read_records(FILENAME, outfile)
        num_list, powerball_list = parse_draw_list(all_draws_list, outfile)
        num_freq_list, pb_freq_list = get_frequencies(num_list, powerball_list, outfile)
        most_freq_num_list = compute_most_freq(num_freq_list, outfile)
        most_freq_pb_list = compute_most_freq(pb_freq_list, outfile)
        least_freq_num_list = compute_least_freq(num_freq_list, outfile)
        least_freq_pb_list = compute_least_freq(pb_freq_list, outfile)
        most_overdue_num_list = get_most_overdue(num_list, outfile)
        most_overdue_pb_list = get_most_overdue(powerball_list, outfile)
        print_stats(num_freq_list, pb_freq_list, most_freq_num_list, most_freq_pb_list, least_freq_num_list, least_freq_pb_list, most_overdue_num_list, most_overdue_pb_list)




###########################################################################
#                           I/O Functions
##########################################################################


# This function uses the for loop to read
# all of the values in a file.
def read_records(filename, outfile):
    row = ''
    all_daily_draws_list = []
    current_draw_list = []


    infile = open(filename, 'r')


    for line in infile:

        row = infile.readline()
        row = row + '\n'
        row = row.split()

        current_draw_list = row
        all_daily_draws_list.append(current_draw_list)

    return all_daily_draws_list


    # Close the file.
    infile.close()

################################################################
def print_stats(num_freq_list, pb_freq_list, most_freq_num_list, most_freq_pb_list, least_freq_num_list, least_freq_pb_list, most_overdue_num_list, most_overdue_pb_list):

    i = 0
    header = 'Most frequent numbers are: '
    listlen=(len(most_freq_num_list))
    print('\n', header, end='')
    for i in range(listlen):
        if i == listlen - 1:
            print(most_freq_num_list[i], end='')
        else:
            print(most_freq_num_list[i], ', ', end='')

    i = 0
    header = 'Most frequent powerball numbers are: '
    print('\nmost_freq_pb_list=', most_freq_pb_list)
    listlen=(len(most_freq_pb_list))
    print('\n', header, end='')
    for i in range(listlen):
        if i == listlen - 1:
            print(most_freq_pb_list[i], end='')
        else:
            print(most_freq_pb_list[i], ', ', end='')

    i = 0
    header = 'Least frequent numbers are: '
    listlen=(len(least_freq_num_list))
    for i in range(listlen):
        if i == listlen - 1:
            print(least_freq_num_list[i], end='')
        else:
            print(least_freq_num_list[i], ', ', end='')



    i = 0
    header = 'Least frequent powerball numbers are: '
    print('\nleast_freq_pb_list=', least_freq_pb_list)
    listlen=(len(least_freq_pb_list))
    print('\n', header, end='')
    for i in range(listlen):
        if i == listlen - 1:
            print(least_freq_pb_list[i], end='')
        else:
            print(least_freq_pb_list[i], ', ', end='')


    i = 0
    header = 'Most overdue numbers are: '
    listlen=(len(most_overdue_num_list))
    print('\n', header, end='')
    for i in range(listlen):
        if i == listlen - 1:
            print(most_overdue_num_list[i], end='')
        else:
            print(most_overdue_num_list[i], ', ', end='')


    i = 0
    header = 'Most overdue numbers are: '
    listlen=(len(most_overdue_pb_list))
    print('\n', header, end='')
    for i in range(listlen):
        if i == listlen - 1:
            print(most_overdue_pb_list[i], end='')
        else:
            print(most_overdue_pb_list[i], ', ', end='')

    print('\n')


#############################################################################
# Processing Functions
#############################################################################

################################################################
def parse_draw_list(input_list, outfile):

    num = ''
    num_list = []
    powerball = ''
    powerball_list = []

    # Loop through input list records
    for i in range(len(input_list)):
        row = input_list[i]

        for n in range(len(row) - 1):
            num = int(row[n])
            num_list.append(num)

        powerball = int(row[len(row) - 1])
        powerball_list.append(powerball)

    return num_list, powerball_list

################################################################
def get_frequencies(numlist, pblist, outfile):

    common_frequency_list = []
    powerball_frequency_list = []


    # sort the common number input list
    sorted_num_list = [] + numlist
    sorted_num_list.sort()
    #print('sorted_num_list =', sorted_num_list)

    # sort the powerball input list
    sorted_pb_list = [] + pblist
    sorted_pb_list.sort()
    #print('sorted_pb_list =', sorted_pb_list)

    listlen = len(sorted_num_list)
    #print('listlen =', listlen)

    position = 0
    n = 0
    count = 0

    # insert 0 count for any possible nums that don't appear in the common ball list
    i = 0
    for i in range(MAX_NUM):
        if i in sorted_num_list == False:
            sorted_num_list.insert(i, count)

    # insert 0 count for any possible nums that don't appear in the powerboll ball list
    i = 0
    for i in range(MAX_PB_NUM):
        if i in sorted_pb_list == False:
            sorted_pb_list.insert(i, count)

    ####### Compute Common Ball Frequencies, append to common_frequency_list #####
    n = 0
    listlen = len(sorted_num_list)
    while n < listlen - 2:
        count = 1
        position += 1
        while sorted_num_list[n] == sorted_num_list[n + 1]:
            count += 1
            position += 1
            n += 1
            if n == listlen - 1:
                break

        common_frequency_list.insert(sorted_num_list[n], count)
        n = position


    ####### Compute PowerBall Frequencies, append to powerball_frequency_list #####
    listlen = len(sorted_pb_list)
    n = 0
    position = 0
    while n < listlen - 2:
        count = 1
        position += 1
        while sorted_pb_list[n] == sorted_pb_list[n + 1]:
            count += 1
            position += 1
            n += 1
            if n == listlen - 1:
                break

        powerball_frequency_list.insert(sorted_pb_list[n], count)
        n = position

    return common_frequency_list, powerball_frequency_list

################################################################
# Function takes a frequency list containing number counts and
# returns the list of 10 most common numbers corresponding to those counts
def compute_most_freq(freq_list, outfile):

    # make a copy of the input frequency list
    frequency_list = [] + freq_list
    most_freq_list = []     # list for storing list of most frequent numbers
    i = 0
    max_count = 0
    max_index = 0

    # select 10 of the most frequent numbers based on counts stored in input frequency list
    for i in range(RANGE):
        max_count = max(frequency_list)                         # highest count in the input list
        max_index = frequency_list.index(max_count)             # index of the highest count
        while max_count in frequency_list and max_count != 0:   # loop through frequency list, looking for the presence of the max_count, but ignore 0s, which are placeholders
            max_index = frequency_list.index(max_count)         # re-grab the index
            most_freq_list.append(max_index + 1)                # append the index of the highest count to the most_freq_list, but add 1 since index starts at 0
            frequency_list.insert(max_index, 0)                 # insert a 0 into the original frequency list at the index of the max count
            frequency_list.remove(max_count)                    # remove max_count from the original list so it's no longer searched

    most_freq_list = most_freq_list[0:RANGE]                    # truncate the list in case the same count was found at multiple indexes

    return most_freq_list

################################################################
# Function takes a frequency list containing number counts and
# returns the list of 10 least common numbers corresponding to those counts
def compute_least_freq(freq_list, outfile):

    # make a copy of the input frequency list
    frequency_list = [] + freq_list
    least_freq_list = []        # list for storing list of least frequent numbers
    i = 0
    min_count = 0
    min_index = 0

    # select 10 of the least frequent numbers based on counts stored in input frequency list
    for i in range(RANGE):
        min_count = min(frequency_list)                         # lowest count in the input list
        min_index = frequency_list.index(min_count)             # index of the lowest count
        while min_count in frequency_list and min_count != 99:  # loop through frequency list, looking for the presence of the min_count, but ignore 99s, which are placeholders
            min_index = frequency_list.index(min_count)         # re-grab the index
            least_freq_list.append(min_index + 1)               # append the index of the lowest count to the least_freq_list, but add 1 since index starts at 0
            frequency_list.insert(min_index, 99)                # insert a 99 into the original frequency list at the index of the min count
            frequency_list.remove(min_count)                    # remove min_count from the original list so it's no longer searched

    least_freq_list = least_freq_list[0:RANGE]                  # truncate the list in case the same count was found at multiple indexes


    return least_freq_list

################################################################
def get_most_overdue(list, outputfile):

    input_list = [] + list
    temp_list = []
    most_overdue_list = []
    listlen = 0
    i = 0
    curr_num = 0

    max_index = 0

    listlen = len(input_list)

    for i in range(listlen):
        curr_num = input_list[i]
        curr_index = input_list.index(curr_num)
        max_index = curr_index
        n =  0

        for n in range(listlen):
            if curr_num == input_list[n]:
                curr_index = n
        max_index = curr_index

        temp_list.append(max_index)


    # Loop through list, and append values corresponding to list of least indexes in temp_list to most_overdue_list
    i = 0
    least_index = 0
    for i in range(listlen):
        least_index = min(temp_list)
        least_value = input_list[least_index]
        if least_value not in most_overdue_list:
            most_overdue_list.append(input_list[least_index])
        temp_list.remove(least_index)

    most_overdue_list = most_overdue_list[0:RANGE]

    return most_overdue_list


####################################################
main()
