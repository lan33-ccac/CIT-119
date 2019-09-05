##################################################################
# Module: State_Capital_Quiz.py
# Exercise: Ch9_Exercise_2.py
# Purpose: Quizes user on state capitals
# Last update: 11/7/18
# Author: Lisa Nydick
##################################################################

#Global constants and variables declarations
state_d_nums = {0:'AL', 1:'AK', 2:'AZ', 3:'AR'}
state_d_abbrev = {'AL':'Montgomery', 'AK':'Juneau', 'AZ':'Pheonix', 'AR':'Little Rock'}

##############################################################################
def main():
    #initialize local variables
    keep_playing = True
    rand = 0
    state_abbrev = ''
    user_answer = ''
    correct_answer = False
    total_answers = 0
    total_correct = 0
    total_incorrect = 0

    while keep_playing == True:
        rand = get_random()
        state_abbrev = state_d_nums.get(rand, 'State not found.')

        if state_abbrev != '':
            user_answer = get_user_input(state_abbrev)

            correct_answer = check_answer(user_answer, state_abbrev)
            total_answers +=1
            if correct_answer:
                total_correct += 1
            else:
                total_incorrect += 1

        else:
            break

        keep_playing = check_keep_playing()

    print_stats(total_correct, total_incorrect)


##############################################################################
def get_random():
    rand_num = 0

    from random import randrange
    rand_num = randrange(0, 3)

    return rand_num

##############################################################################
def get_user_input(state_abbrev):
    answer = ''
    prompt = 'Enter the capital for ' +  state_abbrev + ': '
    reprompt = 'Answer must not be blank.  Try again.'

    while answer == '':
        answer = input(prompt)
        if answer == '':
            print(reprompt)

    return answer

##############################################################################
def check_keep_playing():

    keep_playing = False
    response = ''
    prompt = 'Enter Y to keep playing.'

    response = input(prompt)
    if response == 'Y' or response == 'y':
        keep_playing = True

    return keep_playing

##############################################################################
def check_answer(answer, st):

    correct = False

    if answer.lower() ==  state_d_abbrev[st].lower():
        correct = True
        print('Correct answer.')
    else:
        correct = False
        print('Incorrect answer')

    return correct


##############################################################################
#function for displaying console output
def print_stats(ncorrect, nincorrect):

    print('Total correct responses: ', ncorrect)
    print('Total incorrect responses: ', nincorrect)



##############################################################################
main()
