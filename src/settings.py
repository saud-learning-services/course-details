from dotenv import load_dotenv
import helpers

load_dotenv()
COURSE_ID = helpers.get_course_code()

# project structure folders 
DATA_FOLDER = f'data/{COURSE_ID}'
RAW_FOLDER = f'{DATA_FOLDER}/raw'
PROJECT_FOLDER = f'{DATA_FOLDER}/project_data'

APIOUTPUT_FOLDER = f'{RAW_FOLDER}/api_output' 
NEWANALYTICS_FOLDER = f'{RAW_FOLDER}/new_analytics_input'
GRADEBOOK_FOLDER = f'{RAW_FOLDER}/gradebook_input'

COURSESTRUCTURE_FOLDER = f'{PROJECT_FOLDER}/course_structure'
USERDATA_FOLDER = f'{PROJECT_FOLDER}/user_data'
CLEANEDDATA_FOLDER = f'{PROJECT_FOLDER}/cleaned_data'
TRANSFORMEDDATA_FOLDER = f'{PROJECT_FOLDER}/transformed_data'

# Files created / necessary ... 
COURSESTRUCTURE_FILES = ["assignments.csv","discussion_topics.csv", "external_tools.csv",
            "features.csv", "files.csv", "module_items.csv", "modules.csv", "module_items.csv", "pages.csv",
            "quizzes.csv", "tabs.csv"]

USERDATA_FILES = ["enrollments.csv", "assignment_submissions.csv"]
