##########################################################################
# Module: Write_to_HTML_File.py
# Exercise: Ch6_Exercise_11
# Purpose: Writes input user data to an html file
# CIT-119
# Lisa Nydick
# Last Updated: 10/13/18
##########################################################################

TAGS_START = "<html>\n<head>\n</head>\n<body>\n\t<center>\n\t\t<h1>"
TAGS_MIDDLE = "</h1>\n\t</center>\n\t<hr />\n\t"
TAGS_END = "\n\t<hr />\n</body>\n</html>"
HTML_FILE_NAME = "user.html"

def main():
    user_name = ''
    user_desc = ''
    error_occurred = False
    #Keep asking for input until user provides values for both variables
    while user_name == '' or user_desc == '':
        try:
            user_name, user_desc = get_user_data()
        except KeyboardInterrupt:
            print('You ended the program prematurely.  HTML file was not written')
            error_occurred = True
            break
        except Exception as Err:
            print('Unknown error occurred.  HTML file was not written')
            error_occurred = True
            break

    # Only attempt to write the file if no error occurred
    if error_occurred == False:
        write_file(HTML_FILE_NAME, user_name, user_desc)


# Function reads the user name and description from the console and returns the values to main
def get_user_data():
    your_name = ''
    your_desc = ''
    your_name = input('Enter your name: ')
    your_desc = input('Describe yourself: ')
    return your_name, your_desc

#Function writes the html code and inserts the user name and description in the appropriate places
def write_file(filename, name, desc):

    # Handler for IO type errors
    try:
        outfile = open(filename, 'w')
    except PermissionError:
        print('Cannot create html file due to permission error.')
    except IOError:
        print('An unknown problem occurred when opening the html file for writing.')
    except Exception as err:
        print(err)
    else:
        try:
            outfile.write(TAGS_START)
            outfile.write(name)
            outfile.write(TAGS_MIDDLE)
            outfile.write(desc)
            outfile.write(TAGS_END)
        except PermissionError:
            print('Cannot write to the html file due to permission error.')
        except IOError:
            print('An unknown problem occurred when writing the html file.')
        except Exception as err:
            print(err)
        else:
            print('HTML file was written successfully')

    outfile.close()


main()