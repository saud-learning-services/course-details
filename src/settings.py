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

# Project Data
ORIGINALDATA_FOLDER = f'{PROJECT_FOLDER}/original_data'

APIOUTPUT_FOLDER = f'{ORIGINALDATA_FOLDER}' 

NEWANALYTICS_FOLDER = f'{RAW_FOLDER}/new_analytics_input'
GRADEBOOK_FOLDER = f'{RAW_FOLDER}/gradebook_input'

SCHEMAS_FOLDER = 'schemas' #included in project

CLEANEDDATA_FOLDER = f'{PROJECT_FOLDER}/cleaned_data'