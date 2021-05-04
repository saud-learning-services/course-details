from interface import print_success, print_unexpected, shut_down
from helpers import create_folder, check_for_data

""" 
Once data collected, this script will create a "project_folder"
and reorganize data as appropriate. 
"""
# Given a course_id check that appropriate files exist
# 1. raw/api_output
# 2. raw/new_analytics_input

# create folder called project_data
def create_project_structure(course_id):

    data_folder = f'data/{course_id}'
    
    if check_for_data(data_folder):
        print_success(f'DATA FOLDER FOUND FOR {course_id}\n')
        #folders that should already exist with data in them
        raw_api_data_folder = f'{data_folder}/raw/api_output'
        new_analytics_folder = f'{data_folder}/raw/new_analytics_input'

        # folders that need to be created if don't already
        project_folder = f'{data_folder}/project_folder'
        course_structure_folder = f'{project_folder}/course_structure'
        user_data_folder = f'{project_folder}/user_data'

        print(f'\nATTEMPTING TO CREATE PROJECT STRUCTURE\n')
        if check_for_data(raw_api_data_folder, '\.csv'):
            print(f'{raw_api_data_folder}: At least one csv found, creating project structures.')
            
            msg_list = '\n\t-'.join(
                [create_folder(project_folder),
                create_folder(course_structure_folder),
                create_folder(user_data_folder)]
                )

            print(f'\n\t-{msg_list}')

            #MOVE DATA TO COURSE_STRUCTURE
            #assignments.csv 
            #discussions.csv
            #external_tools.csv
            #features.csv
            #files.csv
            #module_items.csv
            #modules.csv
            #pages.csv
            #quizzes.csv
            #tabs

            # MOVE TO USER_DATA
            #enrollments.csv


        else:
            print_unexpected(f'{raw_api_data_folder}: No csvs found, no project structure to create.')
        
        print(f'\nATTEMPTING TO PARSE NEW ANALYTICS INPUT\n')
        if check_for_data(new_analytics_folder, './csv'):
            print(f'{new_analytics_folder}: New Analytics data found, compiling...')

            # MOVE TO USER_DATA
            #combined new_analytics_input

        else:
            print(f'{new_analytics_folder}: No csvs found.')

    else:
        shut_down(f'NO DATA FOLDER FOUND FOR: {course_id}')

if __name__ == "__main__":
    course_id = input('PLEASE ENTER A COURSE ID: ')
    create_project_structure(course_id)

    # if there is data in new_analytics_input
    # check that all files follow the same structure (column names)
    # given match, create single output