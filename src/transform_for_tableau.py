import pandas as pd
import sys
import json
import numpy as np
import datetime
import re
import ast
from settings import CLEANEDDATA_FOLDER, TABLEAU_FOLDER, INST_CODE
from helpers import create_folder
from interface import print_success

def _extract_file_type(somestring):
    try:
        match_str = re.compile("(.*)(\.)([a-zA-Z]{3}$)") #TODO - 4 chars, i.e) .jpeg
        match = re.match(match_str, somestring)
        if match:
            return(match.group(3))
    except:
        return(None)
    else:
        return(None)

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


def combine_enrollment_and_new_analytics():

    new_analytics =  pd.read_csv(f'{CLEANEDDATA_FOLDER}/new_analytics.csv')
    new_analytics['user_id'] = new_analytics['global_user_id'].apply(lambda x: int(x)-INST_CODE)
    new_analytics['course_id'] = new_analytics['global_course_id'].apply(lambda x: int(x)-INST_CODE)

    enrollment = pd.read_csv(f'{CLEANEDDATA_FOLDER}/enrollments.csv')

    try:
        # filter to active student data only
        
        def get_value(x, key):
            try:
                return(ast.literal_eval(x).get(key))
            except:
                return(None)

        enrollment["student"] = enrollment["user"].apply(lambda x: get_value(x, "name"))

        user_scores = enrollment[["user_id", "student", "user_role", "grades"]].copy()
        
        user_scores["gb_current_score"] = user_scores["grades"].apply(lambda x: get_value(x, "current_score"))
        user_scores["gb_final_score"] = user_scores["grades"].apply(lambda x: get_value(x, "final_score"))
        user_scores = user_scores[["user_id", "student", "user_role", "gb_current_score", "gb_final_score"]]
        user_scores.to_csv(f"{TABLEAU_FOLDER}/user_final_score.csv", index=False)


        enrollment = enrollment[["user_id", "student", "enrollment_type", "enrollment_state"]]
        


        # CREATE USER ORDER ID & FILTER TO STUDENTS
        user_order_df = enrollment.query("enrollment_type=='StudentEnrollment' & enrollment_state=='active'")[["user_id"]]
        user_order_df = user_order_df.reset_index()
        user_order_df.columns = ["user_order_id", "user_id"]
        user_order_df["user_order_id"] = user_order_df["user_order_id"] +1

        enrollment = user_order_df.merge(enrollment, on="user_id", how="left")

        
        student_analytics = enrollment.merge(new_analytics, how="left", on="user_id")
    
        
        keepfiles = [None, "csv", "zip", "txt", "pdf"]  
        student_analytics['filetype'] = student_analytics["content_name"].apply(lambda x: _extract_file_type(x))
        student_analytics = student_analytics.query("`filetype` == @keepfiles")
        output = student_analytics.drop(["global_user_id", "global_course_id"], axis=1)
        output.to_csv(f'{TABLEAU_FOLDER}/student_analytics_noimages.csv', index=False)

        return(student_analytics)
        
    except Exception as e:
        print(f"error: {e}")


def course_assignments_and_dates(student_analytics):
    # NOT USED
    student_analytics = student_analytics[student_analytics['global_user_id'].notna()]

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


def clean_submissions_data():
    gb_info = pd.read_csv(f'{CLEANEDDATA_FOLDER}/assignments.csv')
    gb_info = gb_info.drop(['assignment_description', 'assignment_workflow_state',\
                            'assignment_is_quiz', 'assignment_is_published'], axis=1)

    submissions_df = pd.read_csv(f'{CLEANEDDATA_FOLDER}/assignment_submissions.csv').drop('course_id', axis=1)
    submissions_df = submissions_df.merge(gb_info)

    submissions_df['percent_score'] = submissions_df.apply(lambda x: x['assignment_score']/x['assignment_points_possible'] if x['assignment_points_possible'] > 0 else None, axis=1)
    submissions_df.to_csv(f'{TABLEAU_FOLDER}/student_assignment_details.csv')

def clean_gradebook_data():
    gb_data = pd.read_csv(f'{CLEANEDDATA_FOLDER}/gradebook_user_data.csv') 
    gb_data.to_csv(f"{TABLEAU_FOLDER}/user_final_score.csv", index=False)

def transform_for_tableau_fn():

    create_folder(TABLEAU_FOLDER)
    
    combine_course_structure()
    stud_analytics = combine_enrollment_and_new_analytics()
    #course_assignments_and_dates(stud_analytics) 
    clean_submissions_data()
    #clean_gradebook_data()

    print_success("Data formatted for Tableau complete!")

if __name__ == "__main__":
    transform_for_tableau_fn()