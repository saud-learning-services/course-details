import os
import sys
import re
from termcolor import cprint
from interface import shut_down, print_success
from dotenv import load_dotenv
import hashlib

load_dotenv()

# TO ANONYMIZE
# Canvas output
#   enrollments.csv -> id, user_id, grades, sis_user_id, html_url, user
# User input
#   any analytics files -> sectionName	globalStudentId	studentName	studentSisId
# create 

# create a new output folder course_id-anon
# copy the data into that folder
# apply anonymization to necessary files


def anonymize_data(course_id, string_for_hash, file_name, columns_to_mask, columns_to_drop):
    """[summary]

    Args:
        course_id ([type]): the course id (folder) to look in
        string_for_hash ([type]): the string that will be used to hash all ids
        file_name ([type]): the file to read and apply to
        columns_to_mask ([type]): columns where hash needs to be applied
        columns_to_drop ([type]): columns to drop because provide too much detail
    """    
    


    #
    return

def confirm_anonymizer():
    #TODO - create string in text file for safe keeping
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

def check_for_data(folder, file_regex=None):
    """given a folder and a file string to match
        determines whether the folder exists and at least 
        one file exists matching that regex

    Args:
        folder (str): the string of the folder 
        file_regex (str): some string to match any file if given
    """    

    # check that the folder exists
    
    if os.path.exists(folder):
        if file_regex==None:
            print_success(f'{folder} exists!')
            return(True)
    else:
        print(f'{folder} not found, exiting')
        return(False)



def main():
    COURSE_ID = get_course_code()
    check_for_data(f'output/{COURSE_ID}')
    string_obfuscate = confirm_anonymizer()

# test byte hash sha 256
    hash_object = hashlib.sha256(f'{1001}{string_obfuscate}'.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)

if __name__ == "__main__":
    # execute only if run as a script
    main()