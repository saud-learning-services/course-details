from interface import print_success, print_unexpected
from helpers import create_folder, check_for_data

# Given a COURSE_ID check that appropriate files exist
# 1. raw/api_output
# 2. new_analytics_input

# create folder called project_data


if __name__ == "__main__":
    COURSE_ID = input('PLEASE ENTER A COURSE ID: ')

    #folders that should already exist with data in them
    raw_api_data_folder = f'data/{COURSE_ID}/raw/api_output'
    new_analytics_folder = f'data/{COURSE_ID}/raw/new_analytics_input'

    # folders that need to be created if don't already
    project_folder = f'data/{COURSE_ID}/project_folder'
    course_structure_folder = f'{project_folder}/course_structure'
    user_data_folder = f'{project_folder}/user_data'

    print(f'\nATTEMPTING TO CREATE PROJECT STRUCTURE\n')
    if check_for_data(raw_api_data_folder, '\.csv'):
        print(f'{raw_api_data_folder}: At least one csv found, creating project structures.')
        
        msg_list = '\n\t-'.join([create_folder(project_folder),
            create_folder(course_structure_folder),
            create_folder(user_data_folder)])

        print(f'\n\t-{msg_list}')
        
    
    else:
        print_unexpected(f'{raw_api_data_folder}: No csvs found, no project structure to create.')
    
    print(f'\nATTEMPTING TO PARSE NEW ANALYTICS INPUT\n')
    if check_for_data(new_analytics_folder, './csv'):
        print(f'{new_analytics_folder}: New Analytics data found, compiling...')
    
    else:
        print(f'{new_analytics_folder}: No csvs found.')

    # if there is data in new_analytics_input
    # check that all files follow the same structure (column names)
    # given match, create single output