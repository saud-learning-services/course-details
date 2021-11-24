import pandas as pd
import sys
from helpers import create_folder, schema_rename_and_drop_columns
from settings import COURSE_ID
import settings
import data_details



def transform_data(detail_dict, drop_rest=False):
    # TODO ADD DATE TO FILE AS HEADER
    file = f'{detail_dict["name"]}'
    schema_file = f'{settings.SCHEMAS_FOLDER}/{file}.txt'
    rename_dict = detail_dict["rename_dict"]

    in_file =  f'{settings.ORIGINALDATA_FOLDER}/{file}.csv'
    out_file = f'{settings.CLEANEDDATA_FOLDER}/{file}.csv'


    tem = sys.stdout
    sys.stdout = f = open(f'{settings.CLEANDDATA_TRACKING_TRANSFORMATIONS}/{file}.md', 'w')
    
    print(f'# {file}')
    
    print(f'\nREADING: {in_file}\n')
    df = pd.read_csv(in_file)

    print('## Column Changes')
    df, data_dict = (df.
         pipe(schema_rename_and_drop_columns, rename_dict=rename_dict, schema_file=schema_file, drop_rest=drop_rest))

    print(f'\nWRITING: {out_file}.csv\n')
    df.to_csv(f'{out_file}', index=False)
    data_dict[data_dict['change_note']!='deleted'].to_csv(f'{settings.CLEANDDATA_TRACKING_TRANSFORMATIONS}/{file}_schema.csv', index=False)
    
    sys.stdout = tem
    f.close()
    
    return(df)

# MOST OF THESE FOLDERS NEED TO CHANGE

def main(COURSE_ID):
    create_folder(settings.CLEANEDDATA_FOLDER)
    create_folder(settings.CLEANDDATA_TRACKING_TRANSFORMATIONS)

    transform_data(data_details.ASSIGNMENTS_DICT, True)
    transform_data(data_details.MODULEITEMS_DICT, True)
    transform_data(data_details.MODULES_DICT, True)
    transform_data(data_details.PAGES_DICT, True)
    transform_data(data_details.QUIZZES_DICT, True)
    transform_data(data_details.ASSIGNMENTSUBMISSIONS_DICT, True)
    transform_data(data_details.ENROLLMENTS_DICT, True)
    transform_data(data_details.NEWANALYTICS_DICT, True)
    transform_data(data_details.GRADEBOOKUSERDATA_DICT, True)

if __name__ == "__main__":
    main(COURSE_ID)