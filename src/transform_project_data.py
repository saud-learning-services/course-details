import pandas as pd
import sys
import json
import re
import os
from helpers import get_course_code
from dotenv import load_dotenv


def transform_to_dict(string):
    """For reading and writing to dict a schema .txt file, copied and pasted from Canvas Live API"""
    pattern = "(.*) \((.*), (.*)\): (.*)"
    prog = re.compile(pattern)
    result = prog.match(string)

    my_dict = {"name": result.group(1),
               "data_type": result.group(2),
               "field_description": result.group(4)} 
           
    return(my_dict)

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

def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))

def rename_and_drop_columns(df, rename_dict, schema_file, drop_rest=False): 
    # get column information
    
    schema_df = schema_to_df(schema_file)
    
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


assignments_dict = {
    'id': 'assignment_id',
     'description': 'assignment_description',
     'due_at': 'assignment_due_at',
     'points_possible': 'assignment_points_possible',
     'name': 'assignment_title',
     'submission_types': 'assignment_submission_types',
     'workflow_state': 'assignment_workflow_state',
     'rubric': 'assignment_rubric',
     'is_quiz_assignment': 'assignment_is_quiz',
     'published': 'assignment_is_published',
    'course_id': 'course_id'
}

files_dict = {
    'id': 'file_id',
    'folder_id': 'file_folder_id',
    'display_name': 'file_display_title',
    'content-type': 'file_type',
    'created_at': 'file_created_at'
}

discussion_topics_dict = {
    'id': 'discussion_topic_id',
    'title': 'discussion_topic_title',
    'assignment_id': 'assignment_id',
    'discussion_type': 'discussion_type',
    'published': 'discussion_is_published',
    'course_id': 'course_id'
}

module_items_dict = {
    'id': 'module_item_id',
    'title': 'module_item_title',
    'position': 'module_item_position',
    'type': 'module_item_type',
    'module_id': 'module_id',
    'html_url': 'module_item_html_url',
    'page_url': 'module_item_page_url',
    'url': 'module_item_url',
    'published': 'module_item_published',
    'course_id': 'course_id',
    'content_id': 'module_item_content_id'}

modules_dict = {
    'id': 'module_id',
    'name': 'module_title',
    'position': 'module_position',
    'published': 'module_is_published',
    'course_id': 'course_id'}

pages_dict = {
    'page_id': 'page_id',
    'title': 'page_title',
    'published': 'page_is_published',
    'html_url': 'page_html_url',
    'course_id': 'course_id',
    'url': 'page_url'}

quizzes_dict = {
    'id': 'quiz_id',
    'title': 'quiz_title',
    'description': 'quiz_description',
    'quiz_type': 'quiz_type'
}

assignment_submissions_dict = {
    # NOTE - some changes necessary for not anon dataset!
    'user_id': 'user_id',
    'id': 'assignment_submission_id',
    'score': 'assignment_score',
    'submitted_at': 'assignment_submitted_at',
    'submission_type': 'submission_type',
    'assignment_id': 'assignment_id',
    'workflow_state': 'assignment_submission_status',
    'attempt': 'assignment_attempt',
    'seconds_late': 'assignment_seconds_late',
    'course_id': 'course_id'
}

enrollments_dict = {
    # NOTE - some changes necessary for not anon dataset!
    'user_id': 'user_id',
    'course_id': 'course_id',
    'type': 'enrollment_type',
    'course_section_id': 'enrollment_course_section',
    'role': 'user_role',
    'enrollment_state': 'enrollment_state'
}

new_analytics_dict = {
    # NOTE - some changes necessary for not anon dataset!
    'globalStudentId': 'user_id',
    'globalCourseId': 'global_course_id',
    'contentType': 'content_type',
    'contentName': 'content_name',
    'pageviewCount': 'pageview_count',
    'participationCount': 'participation_count',
    'startDate': 'access_date',
    'lastAccessTime': 'last_access_datetime',
    'firstAccessTime': 'first_access_datetime',
    'file': 'original_data_file'
}

def main(COURSE_ID):

    data_folder = f'data/{COURSE_ID}/project_data'
    user_data_folder = f'{data_folder}/user_data'
    course_structure = f'{data_folder}/course_structure/'
    cleaned_folder = f'{data_folder}/transformed/cleaned_data'

    ## COURSE STRUCTURE FIRST
    transform_data(course_structure, cleaned_folder, "assignments", assignments_dict, "schemas/assignments.txt", True)
    transform_data(course_structure, cleaned_folder, "discussion_topics", discussion_topics_dict, "schemas/discussion_topics.txt", True)
    # skipping external_tools
    # skipping features
    transform_data(course_structure, cleaned_folder, "files", files_dict, "schemas/files.txt", True)
    transform_data(course_structure, cleaned_folder, "module_items", module_items_dict, "schemas/module_items.txt", True)
    transform_data(course_structure, cleaned_folder, "modules", modules_dict,  "schemas/modules.txt", True)
    transform_data(course_structure, cleaned_folder, "pages", pages_dict, "schemas/pages.txt", True)
    transform_data(course_structure, cleaned_folder, "quizzes", quizzes_dict, "schemas/quizzes.txt", True)
    # skipping tabs

    ### USER DATA NEXT
    transform_data(user_data_folder, cleaned_folder, "assignment_submissions", assignment_submissions_dict, "schemas/assignment_submissions.txt", True)
    transform_data(user_data_folder, cleaned_folder, "enrollments", enrollments_dict,  "schemas/enrollents.txt", True)
    transform_data(user_data_folder, cleaned_folder, "new_analytics_user_data_combined", new_analytics_dict, "", True)

if __name__ == "__main__":
    load_dotenv()
    COURSE_ID = get_course_code()
    main(COURSE_ID)