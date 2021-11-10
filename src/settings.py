from dotenv import load_dotenv
import helpers

load_dotenv()
COURSE_ID = helpers.get_course_code()

# project structure folders 
DATA_FOLDER = f'data/{COURSE_ID}'

# top-level folders (project and raw)
PROJECT_FOLDER = f'{DATA_FOLDER}/project_data'
RAW_FOLDER = f'{DATA_FOLDER}/user_input'
# Raw Data

APIOUTPUT_FOLDER = f'{PROJECT_FOLDER}' 
NEWANALYTICS_FOLDER = f'{RAW_FOLDER}/new_analytics_input'
GRADEBOOK_FOLDER = f'{RAW_FOLDER}/gradebook_input'

# Project Data
ORIGINALDATA_FOLDER = f'{PROJECT_FOLDER}/original_data'

# Files created / necessary ... 
COURSESTRUCTURE_FILES = ["assignments.csv","discussion_topics.csv", "external_tools.csv",
            "features.csv", "files.csv", "module_items.csv", "modules.csv", "module_items.csv", "pages.csv",
            "quizzes.csv", "tabs.csv"]

USERDATA_FILES = ["enrollments.csv", "assignment_submissions.csv"]
