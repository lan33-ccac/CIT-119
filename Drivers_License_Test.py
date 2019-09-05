##################################################################
# Module: Drivers_License_Test.py
# Exercise: Ch7_Exercise_7
# Purpose: Checks a student's answers on a driver's license test stored a file with a list of correct answers
# Last update: 10/26/18
# Author: Lisa Nydick
##################################################################

#Global constants and variables declarations
CORRECT_ANSWERS = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
FILENAME = 'student_answers.txt'
SCORE_CUTOFF = 15
PASS = 'Passed'
FAIL = 'Failed'


def main():
    #initialize local variables
    student_answers = []
    wrong_answers = []
    correct_count = 0
    incorrect_count = 0
    outcome = FAIL

    student_answers = read_file()
    print('         ', student_answers)

    student_answers, wrong_answers = compare_scores(student_answers)
    print('Correct: ', CORRECT_ANSWERS)
    print('Wrong:   ', wrong_answers)

    correct_count, outcome = grade_test(wrong_answers)
    incorrect_count = len(wrong_answers) - correct_count

    #print('correct_count = ', correct_count)
    #print('incorrect_count = ', incorrect_count)
    #print('outcome = ', outcome)

    display_output(wrong_answers, outcome, correct_count, incorrect_count)


# This function uses the for loop to read
# all of the values in a file.
def read_file():
    student_answers = []

    # Open the file for reading.
    answers_file = open(FILENAME, 'r')

    # Read all the lines from the file.
    for line in answers_file:
        answer = line.rstrip('\n')
        # Convert line to an int
        student_answers.append(answer)

    # Close the file.
    answers_file.close()


    return student_answers

# function for comparing lists
def compare_scores(student_answers):

    wrong_answers = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

    for i in range(len(student_answers)):
        # Compare lists at equal indexes
        if student_answers[i] != CORRECT_ANSWERS[i]:
            wrong_answers[i] = student_answers[i]
        else:
            wrong_answers[i] = ''

    return student_answers, wrong_answers

# function to grade the test
def grade_test(wrong_list):
    correct_count = 0
    outcome = FAIL

    for i in range(len(wrong_list)):
        if wrong_list[i] == '':
            correct_count += 1

    if correct_count >= 15:
        outcome = PASS
    else:
        outcome = FAIL

    return correct_count, outcome

# function for displaying console output
def display_output(wrong_list, outcome, correct, incorrect):
    question_num = 0
    print('Student', outcome, '.')
    print('Total correct answers =', correct)
    print('Total incorrect answers =', incorrect)
    print('Incorrect answers:')

    for i in range(len(wrong_list)):
        question_num = str(i + 1)
        if wrong_list[i] != '':
            print('Question ' + question_num, ': Correct answer =', CORRECT_ANSWERS[i], ', Student answer =', wrong_list[i])




main()
