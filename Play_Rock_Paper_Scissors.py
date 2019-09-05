###########################################################################
# Module: Play_Rock_Paper_Scissors.py
# Exercise: Ch5_Exercise_21
# Purpose: Plays Rock-Paper-Scissors
# Author: Lisa Nydick
# Last Update: 10/09/2018
###########################################################################

# Global Constants
ROCK = 1
PAPER = 2
SCISSORS = 3
INVALID_SELECTION = 4
TEXT_ROCK = 'rock'
TEXT_PAPER = 'paper'
TEXT_SCISSORS = 'scissors'

############################################
# Function get_computer_selection calls randrange function from the random library to generate a random num between 1 and 3.
# Returns the randomly generated integer for the computer
############################################
def get_computer_selection():
    # import random number library and get random number in range 1-3
    from random import randrange
    computer_selection = randrange(1, 3)
    return computer_selection

############################################
# Function get_user_selection inputs user's selection of rock, paper, or scissors.
# If the input is invalid, keep prompting the user for a valid one.
# If the input is one of the expected 3 values, translate the input text into integers.
# Return the integer representing the selection
############################################
def get_user_selection():
    #initialize user selection to an invalid value so the loop is executed at least once
    user_selection_num = INVALID_SELECTION
    while user_selection_num == INVALID_SELECTION:
        user_selection = input('Make your selection: rock, paper, or scissors')

        # Translate input text to integers
        if user_selection == TEXT_ROCK:
            user_selection_num = ROCK
        elif user_selection == TEXT_PAPER:
            user_selection_num = PAPER
        elif user_selection == TEXT_SCISSORS:
            user_selection_num = SCISSORS
        else:
            user_selection_num = INVALID_SELECTION  #force the loop to repeat
            print('Invalid selection. Enter a valid one.')

    #Return integer representing the computer's choice
    return user_selection_num

############################################
# Function play_game calls the get_computer_selection and get_user_selection values and compares them to see who wins
# Returns nothing (void function)
############################################
def play_game():
    continue_to_play = 'Y'

    #Keep playing until user decides to quit
    while continue_to_play == 'Y':
        computer_num = get_computer_selection() #call function
        user_num = get_user_selection()         #call function

        #Set text to use in messages based on selected options
        if computer_num == ROCK:
            computer_text = TEXT_ROCK
        elif computer_num == PAPER:
            computer_text = TEXT_PAPER
        else:
            computer_text = TEXT_SCISSORS

        #Print the computer's selection
        print('My selection was', computer_text)

        # If both selections are the same, keep looping
        if computer_num == user_num:
            print('Game is a tie, so we must play again')
            continue

        # Compare the computer and user values to determine who wins
        if computer_num == ROCK:
            if user_num == PAPER:
                print('You win.', TEXT_PAPER, 'covers', TEXT_ROCK)
            else: # user_num == SCISSORS
                print('You lose.', TEXT_SCISSORS, 'is smashed by', TEXT_ROCK)
        elif computer_num == PAPER:
            if user_num == ROCK:
                print('You lose.', TEXT_PAPER, 'covers', TEXT_ROCK)
            else: #user_num == SCISSORS
                print('You win.', TEXT_SCISSORS, 'cuts', TEXT_PAPER)
        else: # Computer selected Scissors
            if user_num == ROCK:
                print('You win.', TEXT_ROCK, 'smashes', TEXT_SCISSORS)
            else: #user_num == PAPER
                print('You lose.',  TEXT_ROCK, 'cuts', TEXT_PAPER)

        # Prompt user to see if the game should be replayed.
        continue_to_play = input('Play another game? Y or N')

# Call the play_game function
play_game()