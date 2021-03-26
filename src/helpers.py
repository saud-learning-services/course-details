from pathlib import Path
import os
from os import walk
import re
from interface import print_error, print_success

def create_folder(folder_path):
    print(f'creating {folder_path}')
    Path(folder_path).mkdir(parents=True, exist_ok=True)


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
            print_success(f'{folder_path} exists!')
            return(True)
        else:
            pattern = re.compile(file_regex)
            (_, _, filenames) = next(walk(folder_path))
            all_data_files = [i for i in filenames if re.search(pattern, i)]

            if len(all_data_files) > 0:
                printable_files = '\n\t-'.join(all_data_files)
                print_success(f'Files with match found: \n\t-{printable_files}')
                return(True)
            
            else:
                print_error(f'Folder found, but no match of files')
                return(False)

    else:
        print_error(f'{folder} not found...')
        return(False)