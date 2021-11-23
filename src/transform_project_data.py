import pandas as pd
import sys
from helpers import transform_to_dict, schema_to_df, schema_rename_and_drop_columns
from settings import COURSE_ID
import settings
import data_details



def transform_data(detail_dict, drop_rest=False):
    # TODO ADD DATE TO FILE AS HEADER
    file = f'{detail_dict["name"]}'
    schema_file = f'{file}.txt'
    rename_dict = detail_dict["rename_dict"]

    in_file =  f'{settings.ORIGINALDATA_FOLDER}/{file}.csv'
    out_file = f'{settings.CLEANEDDATA_FOLDER}/{file}.csv'


    tem = sys.stdout
    sys.stdout = f = open(f'{settings.CLEANEDDATA_FOLDER}/{file}.md', 'w')
    
    print(f'# {file}')
    
    print(f'\nREADING: {in_file}\n')
    df = pd.read_csv(in_file)

    print('## Column Changes')
    df, data_dict = (df.
         pipe(schema_rename_and_drop_columns, rename_dict=rename_dict, schema_file=schema_file, drop_rest=drop_rest))

    print(f'\nWRITING: {out_file}.csv\n')
    df.to_csv(f'{out_file}', index=False)
    data_dict[data_dict['change_note']!='deleted'].to_csv(f'{settings.CLEANEDDATA_FOLDER}/{file}_schema.csv', index=False)
    
    sys.stdout = tem
    f.close()
    
    return(df)

# MOST OF THESE FOLDERS NEED TO CHANGE

def main(COURSE_ID):

    data_folder = f'data/{COURSE_ID}/project_data'
    user_data_folder = f'{data_folder}/user_data'
    course_structure = f'{data_folder}/course_structure/'
    cleaned_folder = f'{data_folder}/transformed/cleaned_data'

    transform_data(ASSIGNMENTS_DICT, True)

    ## COURSE STRUCTURE FIRST
    transform_data(course_structure, cleaned_folder, "assignments", data_details.ASSIGNMENTS_DICT, "schemas/assignments.txt", True)
    transform_data(course_structure, cleaned_folder, "discussion_topics", data_details.DISCUSSIONTOPICS_DICT, "schemas/discussion_topics.txt", True)
    # skipping external_tools
    # skipping features
    transform_data(course_structure, cleaned_folder, "files", data_details.FILES_DICT, "schemas/files.txt", True)
    transform_data(course_structure, cleaned_folder, "module_items", data_details.MODULEITEMS_DICT, "schemas/module_items.txt", True)
    transform_data(course_structure, cleaned_folder, "modules", data_details.MODULES_DICT,  "schemas/modules.txt", True)
    transform_data(course_structure, cleaned_folder, "pages", data_details.PAGES_DICT, "schemas/pages.txt", True)
    transform_data(course_structure, cleaned_folder, "quizzes", data_details.QUIZZES_DICT, "schemas/quizzes.txt", True)
    # skipping tabs

    ### USER DATA NEXT
    transform_data(user_data_folder, cleaned_folder, "assignment_submissions", data_details.ASSIGNMENTSUBMISSIONS_DICT, "schemas/assignment_submissions.txt", True)
    transform_data(user_data_folder, cleaned_folder, "enrollments", data_details.ENROLLMENTS_DICT,  "schemas/enrollents.txt", True)
    transform_data(user_data_folder, cleaned_folder, "new_analytics_user_data_combined", data_details.NEWANALYTICS_DICT, "", True)

if __name__ == "__main__":
    main(COURSE_ID)