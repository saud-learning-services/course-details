from get_course_data import create_course_output, create_canvas_object
from transform_project_data import transform_project_data_fn
from helpers import create_config, get_account_courses
from termcolor import cprint
from subaccount_matching import match_course
import pandas as pd




if __name__ == "__main__":
    # Create output in data folder

    canvas = create_canvas_object()
    account = canvas.get_account(454)

    courses_df = get_account_courses(account)
    
    courses_df.to_csv("courses_details.csv")

    COURSE_IDS = list(courses_df['course_id'])

    for course_id in COURSE_IDS:
        config = create_config(course_id, with_user_data=False)
        print(config)
        create_course_output(config)
        transform_project_data_fn(config)



