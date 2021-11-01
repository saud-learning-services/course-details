import pandas as pd
from canvasapi import Canvas
import getpass
import sys
from IPython.display import display, HTML
from datetime import datetime
from interface import shut_down, print_success, _create_csv
from helpers import create_folder

import os
from pathlib import Path
from settings import COURSE_ID
import settings

""" Creates the initial course data which will be output in data/COURSE_ID/raw/api_output 
and creates a new_analytics_input folder for user
"""

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
        
 
def create_df_and_csv(paginatedlist, output_file, filter_to_columns=None, keep=True):
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
        df = pd.DataFrame([i.__dict__ for i in paginatedlist])
        
        # if includes filtered columns list then keep if keep=True
        # or drop if keep=False
        if filter_to_columns:
            
            if keep:
                df = df[filter_to_columns]
            else:
                df.drop(filter_to_columns, axis=1, inplace=True)
        
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
    grades_df = create_df_and_csv(course.get_multiple_submissions(student_ids='all'), f'{output_path}/assignment_submissions')
    

    # discussion topics, entries and replies
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



def create_course_output():
    # establish canvas connection
    canvas, auth_header = create_canvas_object()
    
    #get the course
    # COURSE_ID = settings.COURSE_ID

    #create a project structure for the new course
    course = canvas.get_course(COURSE_ID)
    
    create_folder(settings.APIOUTPUT_FOLDER)
    create_folder(settings.NEWANALYTICS_FOLDER)
    create_folder(settings.GRADEBOOK_FOLDER) 

    get_course_data(course, settings.APIOUTPUT_FOLDER)
    
    print_success("Done! Course data downloaded!")

if __name__ == "__main__":
    # execute only if run as a script
    create_course_output()