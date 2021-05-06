import os
from os import walk
import sys
import re
from termcolor import cprint
from helpers import check_for_data, create_folder, _copy_to_folder, get_course_code
from interface import shut_down, print_success, confirm_strict
from dotenv import load_dotenv
import hashlib
import pandas as pd
from pathlib import Path
from shutil import copyfile


load_dotenv()

""" The goal of this script is to handle anonymization of student data.
    If used, will create an anon folder given a course id,
    this folder will contain anonymized data as well as records of anonymization 
    these records SHOULD NOT BE SHARED (or else the data is no longer anonymous).   

    It handles:
        enrollments 
            id_anon -> id
            dropped_columns -> user_id, grades, sis_user_id, html_url, user
"""

# TO ANONYMIZE
# Canvas output
#   enrollments.csv -> id + 112240000000000000
# User input
#   any analytics files -> globalStudentId	studentName	studentSisId
#   analytics file 
# create 

# create a new output folder course_id-anon
# copy the data into that folder
# apply anonymization to necessary files
# create deanonymizer and script for denonymizing

def _hash_it(string_obfuscate, original_string):
    # test byte hash sha 256
    hash_object = hashlib.sha256(f'{original_string}{string_obfuscate}'.encode())
    hex_dig = hash_object.hexdigest()
    return(hex_dig)

def anonymize_data(course_id, string_for_hash, file_name, id_column_to_mask, columns_to_drop, addUBCID=False):
    """Given a file (found using course_id and file_name) will create an anon version of the file and return 
     an anon df. 

    Args:
        course_id (int): the course id (folder) to look in
        string_for_hash (str): the string that will be used to hash all ids
        file_name (str): the file to read and apply to
        columns_to_mask (list of str): columns where hash needs to be applied
        columns_to_drop (list of str): columns to drop because provide too much detail

    Returns:
        df (dataframe): anonymized dataframe

    Creates:
        csv with given filename in new folder 'output/{course_id}/anon' (.csv)
        a file with the hash string (.txt)
    """    

    #create an anon output folder
    output_folder = f'data/{course_id}/project_data_anonymized/user_data/'
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # read the filename given, mask identified columns drop identified columns, 
    df = pd.read_csv(f'data/{course_id}/project_data/user_data/{file_name}')

    if addUBCID:
        df[id_column_to_mask] = df[id_column_to_mask].apply(lambda x: x + 112240000000000000)

    df[f'{id_column_to_mask}_anon'] = df[id_column_to_mask].apply(lambda x: _hash_it(string_for_hash, x))

    # CREATE KEYS FILES 
    keys_list = columns_to_drop + [id_column_to_mask, f'{id_column_to_mask}_anon']
    df_key = df[keys_list].drop_duplicates()
    
    keys_folder = f'data/{course_id}/project_data_anonymized_keys/'
    Path(keys_folder).mkdir(parents=True, exist_ok=True)
    df_key.to_csv(f'{keys_folder}/key_{file_name}')
    
    df = df.drop(id_column_to_mask, axis=1)
    df = df.drop(columns_to_drop, axis=1)

    # create the output and return the dataframe
    df.to_csv(f'{output_folder}/{file_name}')
    print(f'anon version created: {output_folder}/{file_name}')
    return(df)


def confirm_anonymizer():
    #TODO - create string in text file for safe keeping
    stringinput = input('Please enter a string that will be used to anonymize Canvas User IDs: ')

    cprint(f'\nConfirmation - please copy and store somewhere secret: {stringinput}\n', 'blue')

    confirm_strict('Would you like to continue using the above information?', stringinput)


        
# does a folder exist in output called COURSE_ID
# is there any file in there that.. 
# does a folder exist in the input called COURSE_ID


def anonymizer(COURSE_ID):
    user_data_folder = f'data/{COURSE_ID}/project_data/user_data'
    check_for_data(user_data_folder)

    string_obfuscate = confirm_anonymizer()

    
    # ANONYMIZE 
    #enrollments
    anonymize_data(COURSE_ID, string_obfuscate, 'enrollments.csv', 'user_id', ['id', 'grades', 'html_url', 'user', 'sis_user_id'], True)
    anonymize_data(COURSE_ID, string_obfuscate, 'new_analytics_user_data_combined.csv', 'globalStudentId', ['studentName', 'sortableName', 'studentSisId'])

    
    #MOVE COURSE STRUCTURE FILES TO ANON 
    course_structure_folder_anon = f'data/{COURSE_ID}/project_data_anonymized/course_structure'
    create_folder(course_structure_folder_anon)
    
    course_structure_folder = f'data/{COURSE_ID}/project_data/course_structure'
    (_, _, filenames) = next(walk(course_structure_folder))
    course_structure_files = [i for i in filenames if i.endswith('.csv')]
    
    for i in course_structure_files:
        try:
            _copy_to_folder(course_structure_folder, course_structure_folder_anon, i)
        except:
            print(f"error in copy of {i}")

    print_success("Data successfully anonymized!")

if __name__ == "__main__":
    # execute only if run as a script
    COURSE_ID = get_course_code()
    anonymizer(COURSE_ID)
