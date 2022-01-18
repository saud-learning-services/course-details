import pandas as pd
from canvasapi import Canvas
from IPython.display import display, HTML
from datetime import datetime
from interface import shut_down, print_success
import helpers
import os
from pathlib import Path
from settings import COURSE_ID
import settings
import data_details

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

def get_course_data(course, output_folder, with_user_data=True):

    if with_user_data:
        data_details.ENROLLMENTS_DICT = helpers.create_df_and_csv(course.get_enrollments(), data_details.ENROLLMENTS_DICT, output_folder)
        data_details.ASSIGNMENTSUBMISSIONS_DICT = helpers.create_df_and_csv(course.get_multiple_submissions(student_ids='all'), data_details.ASSIGNMENTSUBMISSIONS_DICT, output_folder)

    data_details.FILES_DICT = helpers.create_df_and_csv(course.get_files(), data_details.FILES_DICT, output_folder)
    #features_df = helpers.create_df_and_csv(course.get_features(), f'{output_path}/features')
    data_details.PAGES_DICT= helpers.create_df_and_csv(course.get_pages(), data_details.PAGES_DICT, output_folder)
    data_details.QUIZZES_DICT= helpers.create_df_and_csv(course.get_quizzes(), data_details.QUIZZES_DICT, output_folder)
    data_details.ASSIGNMENTS_DICT = helpers.create_df_and_csv(course.get_assignments(), data_details.ASSIGNMENTS_DICT, output_folder)
    #externaltools_df = helpers.create_df_and_csv(course.get_external_tools(), f'{output_path}/external_tools')
    #tabs_df = helpers.create_df_and_csv(course.get_tabs() , f'{output_path}/tabs')
    data_details.DISCUSSIONTOPICS_DICT = helpers.create_df_and_csv(course.get_discussion_topics(), data_details.DISCUSSIONTOPICS_DICT, output_folder)
    

    # discussion topics, entries and replies
    #modules and module items
    data_details.MODULES_DICT = helpers.create_df_and_csv(course.get_modules(), data_details.MODULES_DICT, output_folder) # course
    data_details.MODULEITEMS_DICT = helpers.create_df_and_csv(course.get_modules(), data_details.MODULEITEMS_DICT, output_folder, "get_module_items") # course


def create_course_output(canvas, config):
    # establish canvas connection    
    #get the course
    # COURSE_ID = settings.COURSE_ID

    #create a project structure for the new course
    course = canvas.get_course(COURSE_ID)
    
    helpers.create_folder(config["apioutput_folder"])

    if config["with_user_data"]:
        helpers.create_folder(config["newanalytics_folder"])
        helpers.create_folder(config["gradebook_folder"]) 

    get_course_data(course, config["apioutput_folder"], with_user_data=config["with_user_data"])
    
    print_success("Done! Course data downloaded!")

if __name__ == "__main__":
    # execute only if run as a script
    create_course_output()