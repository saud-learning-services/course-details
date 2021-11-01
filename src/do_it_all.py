
from create_project_structure import create_project_structure
from get_course_data import create_course_output
from anonymizer import anonymizer
from interface import confirm_strict, print_success, shut_down
import settings
from settings import COURSE_ID

def do_it_all():
    create_course_output()
    confirm_strict(f"Please add any New Analytics downloads to {settings.NEWANALYTICS_FOLDER}. Confirm when complete enter [Y] or exit [N].")
    confirm_strict(f"Please add your Gradebook export to {settings.GRADEBOOK_FOLDER}. Confirm when complete enter [Y] or exit [N].")
    create_project_structure(COURSE_ID)
    print_success("Done!")

if __name__ == "__main__":
    # execute only if run as a script
    do_it_all()
