import os
import sys
import re
from termcolor import cprint
from interface import shut_down, print_success
from dotenv import load_dotenv

load_dotenv()

def confirm_anonymizer():

    stringinput = input('Please enter a string that will be used to anonymize Canvas User IDs: ')

    cprint(f'\nConfirmation: {stringinput}\n', 'blue')

    confirm = input(
    'Would you like to continue using the above information? [y/n]: \n')

    if confirm == 'y' or confirm == 'Y':
        return(stringinput)
    elif confirm == 'n' or confirm == 'N':
        shut_down('Exiting...')
    else:
        shut_down('ERROR: Only accepted values are y and n')    

def get_course_code():
    try:
        COURSE_ID = os.getenv('COURSE_ID')
        if COURSE_ID == None:
            shut_down('No course ID set, ensure you set it in .env')
        else:
            return(COURSE_ID)
    except Exception:
        shut_down('There was a problem with the .env file. Is there one?')
        
# does a folder exist in output called COURSE_ID
# is there any file in there that.. 
# does a folder exist in the input called COURSE_ID

def check_for_data(folder, file_regex):
    """given a folder and a file string to match
        determines whether the folder exists and at least 
        one file exists matching that regex

    Args:
        folder (str): the string of the folder 
        file_regex (str): some string to match any file
    """    

    # check that the folder exists
    
    if os.path.exists(folder):
        print(f'{folder} exists, looking for files...')
        return(True)
    else:
        print(f'{folder} not found, exiting')
        return(False)

def main():
    COURSE_ID = get_course_code()
    check_for_data(f'output/{COURSE_ID}', 'something')
    confirm_anonymizer()

if __name__ == "__main__":
    # execute only if run as a script
    main()