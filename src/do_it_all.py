
from create_project_structure import create_project_structure
from get_course_data import create_course_output
from interface import confirm_strict, print_success, shut_down
import settings
from settings import COURSE_ID
from transform_project_data import transform_project_data_fn
from transform_for_tableau import transform_for_tableau_fn

def do_it_all():
    create_course_output()
    confirm_strict(f"Please add any New Analytics downloads to {settings.NEWANALYTICS_FOLDER}. Confirm when complete enter [Y] or exit [N].")
    confirm_strict(f"Please add your Gradebook export to {settings.GRADEBOOK_FOLDER}. Confirm when complete enter [Y] or exit [N].")
    create_project_structure()
    transform_project_data_fn()
    transform_for_tableau_fn()
    print_success("Done!")

if __name__ == "__main__":
    # execute only if run as a script
    do_it_all()
