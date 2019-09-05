###########################################################################
# Module: Predict_Pop_Size.py
# Exercise:Ch4_Exercise_13
# Purpose: Predicts Population Size of Organisms
# Author: Lisa Nydick
# Last Update: 10/09/2018
###########################################################################

# initialize input values
num = 0
avg = 0.0
days = 0

#validate each input value
while num <= 0:
    num = int(input('Starting number of organisms'))

#do the same for avg and days

# Input starting values
starting_num = int(input('Enter starting number of organisms'))
daily_increase = int(input('Enter percentage daily increase'))
days_to_multiply = int(input('Enter number of days to multiply'))

#initialize variables to starting values
day = 1
num_organisms = starting_num

# Print heading
print('Day\t\tApproximate Population')

# loop from the first day to number of days the organism will be allowed to multiply 
for n in range(day, days_to_multiply + 1):
    #print the current day and the corresponding number of organisms
    print(day,'\t\t\t', format(num_organisms, '.6f'))
    # set the new number of organisms to be the last number plus the current number of organisms times the daily increase (in percentage)
    num_organisms = num_organisms + (num_organisms * daily_increase / 100)
    #increment the day
    day = day + 1