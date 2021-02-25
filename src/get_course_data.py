import pandas as pd
from canvasapi import Canvas
import getpass
import sys
from IPython.display import display, HTML
from helpers import _create_csv
from datetime import datetime
from interface import shut_down, print_success
from dotenv import load_dotenv
import os
from termcolor import cprint
from pathlib import Path

load_dotenv()

def create_canvas_object(): 
    try:
        url = os.getenv('API_URL')
        token = os.getenv('API_TOKEN')
        auth_header = {'Authorization': f'Bearer {token}'}
        canvas = Canvas(url, token)


        try:
            user = canvas.get_user('self')
            print_success(f'\nHello, {user.name}!')
        except Exception as e:
            shut_down(
                """
                ERROR: could not get user from server.
                Please ensure token is correct and valid and ensure using the correct instance url.
                """
            )
        return(canvas, auth_header)
        
    except Exception as e:
        shut_down(f'{e}: Canvas object not created')
        return(False)
        
 
def create_df_and_csv(paginatedlist, output_file):
    #TODO - figure out "best" structure for this kind of data
    
    """given a list of objects or paginatedlist return a dataframe
    
    Args:
        paginatedlist (a Canvas PaginatedList)
    
    Returns:
        df (dataframe) 
        
    Output:
        csv in output_path if data available
        
    """
    
    try:
        list_of_dicts = []
        for i in paginatedlist:
            i_dict = i.__dict__
            list_of_dicts.append(i_dict)

        df = pd.DataFrame(list_of_dicts)
        df.to_csv(f'{output_file}.csv')
        
        return(df)
        
    except Exception as e:
        print(f'no dataframe for {output_file}: {e}')

def get_course_data(course, output_path):
    enrol_df = create_df_and_csv(course.get_enrollments(), f'{output_path}/enrollments')
    files_df = create_df_and_csv(course.get_files(), f'{output_path}/files')
    features_df = create_df_and_csv(course.get_features(), f'{output_path}/features')
    pages_df = create_df_and_csv(course.get_pages(), f'{output_path}/pages')
    quizzes_df = create_df_and_csv(course.get_quizzes(), f'{output_path}/quizzes')
    assignments_df = create_df_and_csv(course.get_assignments(), f'{output_path}/assignments')
    externaltools_df = create_df_and_csv(course.get_external_tools(), f'{output_path}/external_tools')
    tabs_df = create_df_and_csv(course.get_tabs() , f'{output_path}/tabs')
    discussion_topics_df = create_df_and_csv(course.get_discussion_topics(), f'{output_path}/discussion_topics')

    #modules and module items
    modules = course.get_modules()
    modules_df = create_df_and_csv(modules, f'{output_path}/modules')

    module_items = []

    for m in modules:
        m_items = m.get_module_items()
        
        for i in m_items:
            i_dict = i.__dict__
            module_items.append(i_dict)
            
    module_items_df = pd.DataFrame(module_items)
    module_items_df.to_csv(f'{output_path}/module_items.csv')

def main():
    # establish canvas connection
    canvas, auth_header = create_canvas_object()
    
    #get the course
    COURSE_ID = os.getenv("COURSE_ID")
    course = canvas.get_course(COURSE_ID)
    
    #create an output folder if it doesn't exist
    output_folder = f'output/{COURSE_ID}'
    Path(output_folder).mkdir(parents=True, exist_ok=True)
   
    #create output
    get_course_data(course, output_folder)

if __name__ == "__main__":
    # execute only if run as a script
    main()