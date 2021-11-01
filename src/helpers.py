from pathlib import Path
import os
from os import walk
import re
from interface import print_unexpected, print_success, shut_down
from shutil import copyfile
import pandas as pd
import json

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

def _copy_to_folder(src_folder, dst_folder, file_name, print_details=False):
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
        if print_details:
            print(f'file copied to: {dst_file}')
    
    except Exception as e:
        print(f'Error: {e}')

    return

def create_df_and_csv(paginatedlist, data_dict, output_folder, iteration_call=None):
    #TODO - figure out "best" structure for this kind of data
    
    """given a list of objects or paginatedlist return a dataframe
    
    Args:
        paginatedlist (a Canvas PaginatedList)
        output_file (str)
        filter_to_columns (None or list)
        keep (bool)
    
    Returns:
        df (dataframe) 
        
    Output:
        csv in output_path if data available
        
    """

    try:
        if iteration_call:
            iteration_list = []

            for i in paginatedlist:
                items = getattr(i, iteration_call)

                for j in items():
                    j_dict = j.__dict__
                    iteration_list.append(j_dict)
            
            df = pd.DataFrame(iteration_list)


        else:            
            df = pd.DataFrame([i.__dict__ for i in paginatedlist])


        output_file = f'{output_folder}/{data_dict["name"]}.csv'
        print(output_file)
        data_dict.update({"raw_csv": output_file})
        df.to_csv(f'{output_file}')
        data_dict.update({'df': df})
        return(data_dict)
    
    except Exception as e:
        print(f'{e}')
        return(data_dict.update({"df": None, "raw_csv": None}))

        
def transform_to_dict(string):
    """For reading and writing to dict a schema .txt file, copied and pasted from Canvas Live API"""
    pattern = "(.*) \((.*), (.*)\): (.*)"
    prog = re.compile(pattern)
    result = prog.match(string)

    my_dict = {"name": result.group(1),
               "data_type": result.group(2),
               "field_description": result.group(4)} 
           
    return(my_dict)

def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))