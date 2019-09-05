##################################################################
# Module: Convert_Str_to_Morse_Code.py
# Exercise:Ch8_Exercise_4
# Purpose: Converts an input text strin to Morse code
# Last update: 10/31/18
# Author: Lisa Nydick
##################################################################

#Global constants and variables declarations
MORSE_DICT = {' ': ' ',
              ',': '--..--',
              '.': '._._._',
              '?': '..--..',
              '0': '-----',}



def main():
    #initialize local variables
    fatal_error = False
    inputstring = ''
    morse = ''

    inputstring, fatal_error = get_user_input()
    if fatal_error == False:
        # No fatal error has occurred so keep processing stuff
         morse, fatal_error = convert_str_to_Morse(inputstring)

    if fatal_error == False:
        display_output(morse)


def get_user_input():
    fatal_error = False
    input_string = ''
    while input_string == '':
        try:
            input_string = input('Enter a string to be converted to Morse Code:')
        except ValueError:
            print('Input must be a string')

        except Exception as err:
            print('Unexpected Error:', err, 'occurred. Ending program.')
            fatal_error = True
            input_string = ''
    return input_string, fatal_error


def convert_str_to_Morse(inputstr):
    morseseq = ''
    morsestring = ''
    inputlen = len(inputstr)
    fatal_error = False

    try:
        for i in range(inputlen):
            key = ''
            key = inputstr[i]
            if key in MORSE_DICT.keys():
                morseseq = MORSE_DICT.get(key, 'Key not found')
                print('morseseq=', morseseq)
                morsestring = morsestring + ' ' + morseseq
        i += 1

        print('morsestring=', morsestring)
    except Exception as err:
            print('Unexpected Error:', err, 'occurred. Ending program.')
            fatal_error = True
            morsestring = ''
    return morsestring, fatal_error



# function for displaying console output
def display_output(morsestring):

    print('Morse code conversion =', morsestring)




main()