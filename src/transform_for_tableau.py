import pandas as pd
import sys
import json
import numpy as np
import datetime
import re
from settings import COURSE_ID, CLEANEDDATA_FOLDER, TABLEAU_FOLDER

def _parse_date_time(str):
    try:
        date = datetime.datetime.strptime(str, "%Y-%m-%dT%H:%M:%SZ")
        date = format(date, "%Y-%m-%d")
        return(date)
    except:
        pass

def combine_course_structure():

    module_items = pd.read_csv(f'{CLEANEDDATA_FOLDER}/module_items.csv')
    modules = pd.read_csv(f'{CLEANEDDATA_FOLDER}/modules.csv')
    modules_and_items = module_items.merge(modules, on=["course_id", "module_id"])
    modules_and_items['item_order'] = modules_and_items.apply(lambda x: x['module_position'] 
                                                            + x['module_item_position']/100, axis=1)
    modules_and_items['item_overall_order'] = np.arange(len(modules_and_items.sort_values('item_order')))
    modules_and_items.to_csv(f'{TABLEAU_FOLDER}/module_and_items.csv', index=False)

    CLEANEDDATA_FOLDER = 'cleaned_data'
    TABLEAU_FOLDER = f'transformed_data'

def combine_enrollment_and_new_analytics():

    new_analytics =  pd.read_csv(f'{CLEANEDDATA_FOLDER}/new_analytics_user_data_combined.csv')

    enrollment = pd.read_csv(f'{CLEANEDDATA_FOLDER}/enrollments.csv')

    # filter to active student data only
    enrollment = enrollment.query("enrollment_type=='StudentEnrollment' & enrollment_state=='active'")[["user_id"]]
    enrollment = enrollment.reset_index()
    enrollment.columns = ["user_order_id", "user_id"]
    enrollment["user_order_id"] = enrollment["user_order_id"] +1
    student_analytics = enrollment.merge(new_analytics, how="left", on="user_id")

    def extract_file_type(somestring):
        match_str = re.compile("(.*)(\.)([a-zA-Z]{3}$)") 
        match = re.match(match_str, somestring)
        if match:
            return(match.group(3))
        else:
            return(None)
        
    keepfiles = [None, "csv", "zip", "txt", "pdf"]    
    student_analytics['filetype'] = student_analytics["content_name"].apply(lambda x: extract_file_type(x))
    student_analytics = student_analytics.query(f'filetype=={keepfiles}')
    student_analytics.to_csv(f'{TABLEAU_FOLDER}/student_analytics_noimages.csv', index=False)

def course_assignments_and_dates():
    first_date = student_analytics['access_date'].min()
    last_date = student_analytics['access_date'].max()
    all_dates = pd.date_range(start=first_date,end=last_date, freq="D").date.tolist()

    dates_df = pd.DataFrame({"date": all_dates})
    dates_df["date"] = dates_df["date"].apply(lambda x: str(x))

    assignments = pd.read_csv(f'{CLEANEDDATA_FOLDER}/assignments.csv')
    assignments = assignments[['assignment_id', 'assignment_due_at', 'assignment_title']]

        
        

    assignments['date'] = assignments['assignment_due_at'].apply(lambda x: _parse_date_time(x))
    dates_df = dates_df.merge(assignments, on="date", how="left")
    dates_df.to_csv(f"{TABLEAU_FOLDER}/course_dates.csv")

    gb_info = pd.read_csv('cleaned_data/assignments.csv')
    gb_info = gb_info.drop(['assignment_description', 'assignment_workflow_state', 'assignment_rubric',\
                            'assignment_is_quiz', 'assignment_is_published'], axis=1)

def clean_submissions_data():
    submissions_df = pd.read_csv('cleaned_data/assignment_submissions.csv').drop('course_id', axis=1)
    submissions_df = submissions_df.merge(gb_info)

    submissions_df['percent_score'] = submissions_df.apply(lambda x: x['assignment_score']/x['assignment_points_possible'] if x['assignment_points_possible'] > 0 else None, axis=1)
    submissions_df.to_csv('transformed_data/student_assignment_details.csv')

def clean_gradebook_data():
    gb_data = pd.read_csv('project_data_anonymized/user_data/gradebook_user_data.csv')
    gb_data['user_id'] = gb_data['ID_anon'] 
    final_scores = gb_data[['user_id', 'Current Score', 'Final Score']]
    final_scores.to_csv("transformed_data/user_final_score.csv", index=False)