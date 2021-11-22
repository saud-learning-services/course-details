from interface import print_success, print_unexpected, shut_down
from helpers import create_folder, check_for_data, _copy_to_folder
import glob
import pandas as pd
from settings import COURSE_ID
import settings
import re
from os import walk

""" 
Once data collected, this script will create a "project_folder"
and reorganize data as appropriate. 
"""
        
# create folder called project_data
def create_project_structure(course_id):
    
    if check_for_data(settings.DATA_FOLDER):
        print_success(f'DATA FOLDER FOUND FOR {course_id}\n')
        
        print(f'\nAttempting to parse new analytics data...\n')
        if check_for_data(settings.NEWANALYTICS_FOLDER, '.csv'):
            print_success(f'{settings.NEWANALYTICS_FOLDER}: New Analytics data found, compiling...')

            # MOVE TO USER_DATA
            #combined new_analytics_input
            analytics_files = glob.glob(f"{settings.NEWANALYTICS_FOLDER}/*.csv")
            li = []
            for filename in analytics_files:
                df = pd.read_csv(filename)
                df['file'] = filename
                li.append(df)

            df = pd.concat(li, axis=0)
            df.to_csv(f"{settings.ORIGINALDATA_FOLDER}/new_analytics.csv")
 
        else:
            print(f'{settings.NEWANALYTICS_FOLDER}: No csvs found.')

        if check_for_data(settings.GRADEBOOK_FOLDER, '.csv'):
            print_success(f'{settings.GRADEBOOK_FOLDER}: Gradebook data found, compiling...')

            #TODO look for a single csv file in gradebook_folder
            gb_detail = pd.read_csv(f'{settings.GRADEBOOK_FOLDER}/gradebook.csv', nrows=2)
            column_names = list(gb_detail.columns)
            gb_user = pd.read_csv(f'{settings.GRADEBOOK_FOLDER}/gradebook.csv', names = column_names, skiprows=3)

            gb_user.to_csv(f"{settings.ORIGINALDATA_FOLDER}/gradebook_user_data.csv", index=False)
            gb_detail.to_csv(f"{settings.ORIGINALDATA_FOLDER}/gradebook_details.csv", index=False)

        else:
            print(f'{settings.GRADEBOOK_FOLDER}: No csvs found.')

    else:
        shut_down(f'NO DATA FOLDER FOUND FOR: {course_id}')


if __name__ == "__main__":
    create_project_structure(COURSE_ID)

    # if there is data in new_analytics_input
    # check that all files follow the same structure (column names)
    # given match, create single output