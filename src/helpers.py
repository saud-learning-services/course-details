from pathlib import Path
import os
from os import walk
import re
from interface import print_unexpected, print_success, shut_down
from shutil import copyfile
from yaspin import yaspin
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
                print_success(f'SUCCESS: At least one file found! {printable_files}')
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
    output_file = f'{output_folder}/{data_dict["name"]}.csv'

    try:
        if iteration_call:
            iteration_list = []

            with yaspin(text=f"Generating: {output_file}"):
                for i in paginatedlist:
                    items = getattr(i, iteration_call)

                    for j in items():
                        j_dict = j.__dict__
                        iteration_list.append(j_dict)
            
            df = pd.DataFrame(iteration_list)


        else:            
            with yaspin(text=f"Generating: {output_file}"):
                df = pd.DataFrame([i.__dict__ for i in paginatedlist])


        print_success(f"Generated: {output_file}")
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

def schema_to_df(file):
    """For reading and writing to dict a schema .txt file, copied and pasted from Canvas Live API"""
    try:
        f = open(file, "r")
        lines = f.readlines()
        data = []
        for index, line in enumerate(lines):
            try:
                data.append(transform_to_dict(line))
            except:
                pass

        f.close()
        df = pd.DataFrame(data)
        df['schema_file'] = file
        return(df)
    except Exception as e:
        print(f"Error for {file}: {e}")

def schema_rename_and_drop_columns(df, rename_dict, schema_file, drop_rest=False): 
    # get column information
    
    schema_df = schema_to_df(schema_file)

    og_cols = df.columns.to_list()
    keep_cols = list(rename_dict.keys())
    unlisted_cols = list(set(og_cols) - set(keep_cols))
    has_dropped = False
    
    # changes if dropping 
    if drop_rest:
        print("DROPPING UNLISTED COLS")
        dropped_cols = unlisted_cols
        # change record
        if dropped_cols:
            has_dropped = True
            dropped_df = pd.DataFrame(dropped_cols)
            dropped_df.columns = ['original']
            dropped_df['change_note'] = 'deleted'

        # changed_cols_df = changed_cols_df.append(dropped_df, ignore_index=True)
        # make change
        df = df[keep_cols].copy() 
    
    else:
        print("KEEPING UNLISTED COLS")
        unlisted_dict = dict(zip(unlisted_cols, unlisted_cols))
        rename_dict.update(unlisted_dict)
        
    changed_cols_df = pd.DataFrame.from_dict(rename_dict, orient='index').reset_index()
    changed_cols_df.columns = ['original', 'current']
    changed_cols_df['change_note'] = changed_cols_df.apply(
        lambda x: 'renamed' 
        if x['current']!=x['original'] 
        else 'no_change', 
        axis=1)
    
    if has_dropped & drop_rest:
        changed_cols_df = changed_cols_df.append(dropped_df, ignore_index=True)
        
    try:    
        changed_cols_df = changed_cols_df.merge(schema_df, how="left", left_on="original", right_on="name")
    except Exception as e:
        print(f"error finding data schema: {e}")
        pass
    
    print(changed_cols_df.to_markdown())
    df.rename(rename_dict, axis=1, inplace=True)
    return(df, changed_cols_df)
    
def create_config(course_id, with_user_data=True):
    data_folder = f'data/{course_id}'

    project_folder = f'{data_folder}/project_data'
    raw_folder = f'{data_folder}/user_input'

    originaldata_folder = f'{project_folder}/original_data'
    apioutput_folder = f'{originaldata_folder}' 

    newanalytics_folder = f'{raw_folder}/new_analytics_input'
    gradebook_folder = f'{raw_folder}/gradebook_input'

    schemas_folder = 'schemas' #included in project

    cleaneddata_folder = f'{project_folder}/cleaned_data'
    cleaneddata_tracking_transformations = f'{cleaneddata_folder}/transformations'

    tableau_folder = f'{project_folder}/tableau_data'

    return {
        "course_id": course_id,
        "data_folder": data_folder,
        "project_folder": project_folder,
        "raw_folder": raw_folder,
        "originaldata_folder": originaldata_folder,
        "apioutput_folder": apioutput_folder,
        "newanalytics_folder": newanalytics_folder,
        "gradebook_folder": gradebook_folder,
        "schemas_folder": schemas_folder,
        "cleaneddata_folder": cleaneddata_folder,
        "cleaneddata_tracking_transformations": cleaneddata_tracking_transformations,
        "tableau_folder": tableau_folder,
        "with_user_data": with_user_data
    }