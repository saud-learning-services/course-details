from interface import print_success, print_unexpected, shut_down
from helpers import create_folder, check_for_data, _copy_to_folder, get_course_code
import glob
import pandas as pd

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
        project_folder = f'{data_folder}/project_data'
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
            course_structure_files = ["assignments.csv", "discussion_topics.csv", "external_tools.csv",
            "features.csv", "files.csv", "module_items.csv", "modules.csv", "module_items.csv", "pages.csv",
            "quizzes.csv", "tabs.csv"]

            for i in course_structure_files:
                try:
                    _copy_to_folder(raw_api_data_folder, course_structure_folder, i)
                except:
                    print(f"error in copy of {i}")

            # MOVE TO USER_DATA
            user_data_files = ["enrollments.csv"]
            for i in user_data_files:
                _copy_to_folder(raw_api_data_folder, user_data_folder, i)

        else:
            print_unexpected(f'{raw_api_data_folder}: No csvs found, no project structure to create.')
        
        print(f'\nATTEMPTING TO PARSE NEW ANALYTICS INPUT\n')
        if check_for_data(new_analytics_folder, '.csv'):
            print(f'{new_analytics_folder}: New Analytics data found, compiling...')

            # MOVE TO USER_DATA
            #combined new_analytics_input
            analytics_files = glob.glob(f"{new_analytics_folder}/*.csv")
            print(analytics_files)
            li = []
            for filename in analytics_files:
                df = pd.read_csv(filename)
                df['file'] = filename
                li.append(df)

            df = pd.concat(li, axis=0)
            df.to_csv(f"{user_data_folder}/new_analytics_user_data_combined.csv")

        else:
            print(f'{new_analytics_folder}: No csvs found.')

    else:
        shut_down(f'NO DATA FOLDER FOUND FOR: {course_id}')

if __name__ == "__main__":
    COURSE_ID = get_course_code()
    create_project_structure(COURSE_ID)

    # if there is data in new_analytics_input
    # check that all files follow the same structure (column names)
    # given match, create single output