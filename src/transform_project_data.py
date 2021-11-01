import pandas as pd
import sys
from helpers import transform_to_dict
from settings import COURSE_ID
import data_details


def schema_to_df(file):
    """For reading and writing to dict a schema .txt file, copied and pasted from Canvas Live API"""
    try:
        f = open(file, "r")
        lines = f.readlines()
        data = []
        for index, line in enumerate(lines):
            try:
                data.append(transform_to_dict(line))
            except:
                pass

        f.close()
        df = pd.DataFrame(data)
        df['schema_file'] = file
        return(df)
    except Exception as e:
        print(f"Error for {file}: {e}")


def rename_and_drop_columns(df, rename_dict, schema_file, drop_rest=False): 
    # get column information
    
    schema_df = schema_to_df(schema_file)
    rename_dict = rename_dict["rename_dict"]
    og_cols = df.columns.to_list()
    keep_cols = list(rename_dict.keys())
    unlisted_cols = list(set(og_cols) - set(keep_cols))
    has_dropped = False
    
    # changes if dropping 
    if drop_rest:
        print("DROPPING UNLISTED COLS")
        dropped_cols = unlisted_cols
        # change record
        if dropped_cols:
            has_dropped = True
            dropped_df = pd.DataFrame(dropped_cols)
            dropped_df.columns = ['original']
            dropped_df['change_note'] = 'deleted'

        # changed_cols_df = changed_cols_df.append(dropped_df, ignore_index=True)
        # make change
        df = df[keep_cols].copy() 
    
    else:
        print("KEEPING UNLISTED COLS")
        unlisted_dict = dict(zip(unlisted_cols, unlisted_cols))
        rename_dict.update(unlisted_dict)
        
    changed_cols_df = pd.DataFrame.from_dict(rename_dict, orient='index').reset_index()
    changed_cols_df.columns = ['original', 'current']
    changed_cols_df['change_note'] = changed_cols_df.apply(
        lambda x: 'renamed' 
        if x['current']!=x['original'] 
        else 'no_change', 
        axis=1)
    
    if has_dropped & drop_rest:
        changed_cols_df = changed_cols_df.append(dropped_df, ignore_index=True)
        
    try:    
        changed_cols_df = changed_cols_df.merge(schema_df, how="left", left_on="original", right_on="name")
    except Exception as e:
        print(f"error finding data schema: {e}")
        pass
    
    print(changed_cols_df.to_markdown())
    df.rename(rename_dict, axis=1, inplace=True)
    return(df, changed_cols_df)
    

def transform_data(in_folder, out_folder, file, rename_dict, schema_file, drop_rest=False):
    # TODO ADD DATE TO FILE AS HEADER
    in_file =  f'{in_folder}/{file}.csv'
    out_file = f'{out_folder}/{file}.csv'


    tem = sys.stdout
    sys.stdout = f = open(f'{out_folder}/{file}.md', 'w')
    
    print(f'# {file}')
    
    print(f'\nREADING: {in_file}\n')
    df = pd.read_csv(in_file)

    print('## Column Changes')
    df, data_dict = (df.
         pipe(rename_and_drop_columns, rename_dict=rename_dict, schema_file=schema_file, drop_rest=drop_rest))

    print(f'\nWRITING: {out_file}.csv\n')
    df.to_csv(f'{out_file}', index=False)
    data_dict[data_dict['change_note']!='deleted'].to_csv(f'{out_folder}/{file}_schema.csv', index=False)
    
    sys.stdout = tem
    f.close()
    
    return(df)



def main(COURSE_ID):

    data_folder = f'data/{COURSE_ID}/project_data'
    user_data_folder = f'{data_folder}/user_data'
    course_structure = f'{data_folder}/course_structure/'
    cleaned_folder = f'{data_folder}/transformed/cleaned_data'

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