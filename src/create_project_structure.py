from interface import print_success, shut_down
from helpers import check_for_data
import glob
import pandas as pd

""" 
Once data collected, this script will create a "project_folder"
and reorganize data as appropriate. 
"""
        
# create folder called project_data
def create_project_structure(config):
    
    if check_for_data(config["data_folder"]):
        print_success(f'DATA FOLDER FOUND {config["data_folder"]}\n')
        
        print(f'\nAttempting to parse new analytics data...\n')
        if check_for_data(config["newanalytics_folder"], '.csv'):
            print_success(f'{config["newanalytics_folder"]}: New Analytics data found, compiling...')

            # MOVE TO USER_DATA
            #combined new_analytics_input
            analytics_files = glob.glob(f'{config["newanalytics_folder"]}/*.csv')
            li = []
            for filename in analytics_files:
                df = pd.read_csv(filename)
                df['file'] = filename
                li.append(df)

            df = pd.concat(li, axis=0)
            df.to_csv(f'{config["originaldata_folder"]}/new_analytics.csv')
 
        else:
            print(f'{config["newanalytics_folder"]}: No csvs found.')

        if check_for_data(config["gradebook_folder"], '.csv'):
            print_success(f'{config["gradebook_folder"]}: Gradebook data found, compiling...')

            #TODO look for a single csv file in gradebook_folder
            gb_detail = pd.read_csv(f'{config["gradebook_folder"]}/gradebook.csv', nrows=2)
            column_names = list(gb_detail.columns)
            gb_user = pd.read_csv(f'{config["gradebook_folder"]}/gradebook.csv', names = column_names, skiprows=3)

            gb_user.to_csv(f'{config["originaldata_folder"]}/gradebook_user_data.csv', index=False)
            gb_detail.to_csv(f'{config["originaldata_folder"]}/gradebook_details.csv', index=False)

        else:
            print(f'{config["gradebook_folder"]}: No csvs found.')

    else:
        shut_down(f'NO DATA FOLDER FOUND FOR: {config["data_folder"]}')


if __name__ == "__main__":
    create_project_structure()

    # if there is data in new_analytics_input
    # check that all files follow the same structure (column names)
    # given match, create single output