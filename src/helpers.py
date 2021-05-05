from pathlib import Path
import os
from os import walk
import re
from interface import print_unexpected, print_success
from shutil import copyfile

def get_course_code():
    try:
        COURSE_ID = os.getenv('COURSE_ID')
        if COURSE_ID == None:
            shut_down('No course ID set, ensure you set it in .env')
        else:
            return(COURSE_ID)
    except Exception:
        shut_down('There was a problem with the .env file. Is there one?')
        
def create_folder(folder_path):
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    return(f'creating {folder_path}')

def check_for_data(folder_path, file_regex=None):
    """given a folder and a file string to match
        determines whether the folder exists and at least 
        one file exists matching that regex

    Args:
        folder (str): the string of the folder 
        file_regex (str): some string to match any file if given
    """    

    # check that the folder exists
    
    if os.path.exists(folder_path):
        if file_regex==None:
            print_success(f'SUCCESS: Folder, {folder_path}, exists.')
            return(True)
        else:
            pattern = re.compile(file_regex)
            (_, _, filenames) = next(walk(folder_path))
            all_data_files = [i for i in filenames if re.search(pattern, i)]

            if len(all_data_files) > 0:
                printable_files = '\n\t-'.join(all_data_files)
                #print(f'Files with match found: \n\t-{printable_files}')
                print_success(f'SUCCESS: At least one file found!')
                return(True)
            
            else:
                print_unexpected(f'FAIL: Folder {folder_path} found, but no matching files {file_regex}.')
                return(False)

    else:
        print_unexpected(f'FAIL: Folder, {folder_path}, not found...')
        return(False)

def _copy_to_folder(src_folder, dst_folder, file_name):
    """[summary]

    Args:
        src_folder ([type]): [description]
        dst_folder ([type]): [description]
        file_name ([type]): [description]
    """  
    #TODO - implement
    Path(dst_folder).mkdir(parents=True, exist_ok=True)

    src_file = f'{src_folder}/{file_name}'
    dst_file = f'{dst_folder}/{file_name}'

    try:
        copyfile(src_file, dst_file)
        print(f'file copied to: {dst_file}')
    
    except Exception as e:
        print(f'Error: {e}')

    return