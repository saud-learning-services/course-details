
from create_project_structure import create_project_structure
from get_course_data import create_course_output
from interface import confirm_strict, print_success, shut_down
import settings
from settings import COURSE_ID
from transform_project_data import transform_project_data_fn
from transform_for_tableau import transform_for_tableau_fn
from helpers import create_config

def do_it_all():
    config = create_config(COURSE_ID)
    create_course_output(config)
    confirm_strict(f'Please add any New Analytics downloads to {config["newanalytics_folder"]}. Confirm when complete enter [Y] or exit [N].')
    confirm_strict(f'Please add your Gradebook export to {config["gradebook_folder"]}. Confirm when complete enter [Y] or exit [N].')
    create_project_structure(config)
    transform_project_data_fn(config)
    transform_for_tableau_fn(config)
    print_success("Done!")

if __name__ == "__main__":
    # execute only if run as a script
    do_it_all()
