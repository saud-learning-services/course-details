
from create_project_structure import create_project_structure
from get_course_data import create_course_output
from anonymizer import anonymizer
from interface import confirm_strict, print_success, shut_down

def do_it_all():
    COURSE_ID, new_analytics_folder = create_course_output()
    confirm_strict(f"Please add any New Analytics downloads to {new_analytics_folder}. Confirm when complete enter [Y] or exit [N].")
    create_project_structure(COURSE_ID)
    anonymizer(COURSE_ID)

    print_success("Done!")

if __name__ == "__main__":
    # execute only if run as a script
    do_it_all()
