
# Canvas Course Details

> THIS IS A WIP PROJECT
> Questions? Talk to Alison :) 

Given a course id, extracts details of course including:

- assignments
- quizzes
- pages
- enrollments
- tabs (navigation)
- external tools
- features
- discussion_topics *WIP*
- modules
- module_items
- files

## Use

### First Time

1. We use conda, and suggest miniconda for your projects: [Install Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. We also like VSCode: [Install VSCode](https://code.visualstudio.com/)
3. Clone this project
4. Create the environment `canvas-get-course-details` (in terminal) 
> In terminal: `$ conda env create -f environment.yml`
5. In this project folder (canvas-course-details), create a .env file with the following, save in canvas-course-details folder
```
COURSE_ID = your_course_id
API_URL = 'https://ubc.instructure.com'
API_TOKEN = 'your_token'
```
> Your token should be kept private and secure. We recommend setting expiry on your tokens, and deleting from Canvas once no longer needed. 

### Every Time
1. Make sure you have set `your_course_id` in the .env file
2. Create a new token and add it to API_TOKEN in .env
> i.e `API_TOKEN = 'some string here'`

In terminal:
1. Make sure you are in the right directory
> `$ cd canvas-course-details`
2. Activate the environment
> `$ conda activate canvas-get-course-details`
3. Run the script! (In terminal:)
> `$ python src/get_course_data.py` 
