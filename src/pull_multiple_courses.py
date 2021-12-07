from get_course_data import create_course_output, create_canvas_object
from transform_project_data import transform_project_data_fn
from helpers import create_config
from termcolor import cprint
from subaccount_matching import match_course
import pandas as pd

COURSE_IDS = ["10456", "51614", "77752"]

def create_subaccount_output(list_of_course_ids):
    data = []
    canvas, _ = create_canvas_object()
    for course_id in list_of_course_ids:
        course = canvas.get_course(course_id)
        cprint(f"Getting subaccount info for {course.name}({course_id})", "green")
        subaccount_name, subaccount_id = match_course(course.name)
        row = {
            "course_id": course_id,
            "course_name": course.name,
            "subaccount_name": subaccount_name,
            "subaccount_id": subaccount_id
        }
        data.append(row)
    
    df = pd.DataFrame(data=data)
    df.to_csv(f"data/subaccount_info.csv", index=False)



if __name__ == "__main__":
    # Create output in data folder
    for course_id in COURSE_IDS:
        config = create_config(course_id, with_user_data=False)
        create_course_output(config)
        transform_project_data_fn(config)
    
    # Create subaccount info CSV ["course_id", "course_name", "subaccount_name", "subaccount_id"]
    create_subaccount_output(COURSE_IDS)



