
# Canvas Course Details

> THIS IS A WIP PROJECT
> Questions? Talk to Alison :) 

Given a course id, extracts details of course including:

## Goals
3 levels of "data" 
1. Skeleton 
2. Course Details
3. Student Details
4. Student Interaction -> outside of scope of API data (aspirational)

## 🗂 Data Structures
### Skeleton
- assignments
- quizzes
- pages
- enrollments
- tabs (navigation)
- *external tools* 
- features
- discussion_topics
- modules
- module_items
- files

### Course Details
- page_links *TODO*
- quiz_details *TODO*
- assignment_details *TODO*
### Student Details
- student_discussion_responses *TODO*
- student_quiz_submissions *TODO*
- student_assignment_submissions *TODO*

### Student Interaction
- *TODO*: A user can download student interaction data in Canvas from New Analytics. Given that the data is downloaded consistently (Canvas only has 27 days in New Analytics), and stored in `input`, the goal is to be able to combine student interaction with other course and student data for a "full picture" of the course and its activity. 

![shows relationship between scope](img/simple_project_scope.png)

## 🚀 Use
### Computer Setup

1. We use conda, and suggest miniconda for your projects: [Install Miniconda](https://docs.conda.io/en/latest/miniconda.html) -> whichever the latest 3.x version is, use the 'pkg' version if you are unfamiliar with bash
2. We also like VSCode: [Install VSCode](https://code.visualstudio.com), and the [Python Extension](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites)
3. You also need to have Git installed. We like [GitHub Desktop](https://desktop.github.com/) if you aren't familiar with terminal

### Project Setup
1. Clone this project
2. Create the environment `canvas-get-course-details` (in terminal) 
> `$ conda env create -f environment.yml`
1. In this project folder (course-details), create a .env file with the following, save in course-details folder
```
COURSE_ID = your_course_id
API_URL = 'https://ubc.instructure.com'
API_TOKEN = 'your_token'
```
> ⚠️ Your token should be kept private and secure. We recommend setting expiry on your tokens, and deleting from Canvas once no longer needed. 

Creating a .env file in VSCode is easy. in the File Explorer right click, add a new file. The file is called .env, and then you can edit it as needed in the editor window.
![image_of_env_file](img/create_env_file.png)

### Every Time
1. This project is under active development -> Make sure you've pulled the latest version
2. Make sure you have set `your_course_id` in the .env file
3. Create a new token and add it to API_TOKEN in .env

![image of how to get a token](img/create_a_token.png)

> i.e `API_TOKEN = 'some string here'`

4. Run the script(s)
In terminal:
   i. Make sure you are in the right directory (if you opened the folder in vscode and see the project files in the explorer, then you are in the right directory) - check with the command:
   > `$ pwd`

   if you are not in the right directory, you can use `cd` in terminal to navigate, for example if the project is in Documents/GitHub/course-details

   > `$ cd "Documents/GitHub/course-details"` 
   
   ii. Activate the environment
   > `$ conda deactivate`
   > `$ conda activate canvas-get-course-details`
   
   iii. Run the scripts! (In terminal:)
<br>

   a) The first script gets the data from Canvas and creates your first set of folders in **data**. 
   > `$ python src/get_course_data.py` 

   If all goes well, you should see Hello <your_name_here>! and a new folder in the output with the given course_id and the data. 

   ![image_of_env_file](img/step-a-folder-output.png)
<br>

   b) Once run successfully, you should have a folder data/COURSE_ID/raw/new_analytics_input. 
   > Add any new analytics files you have downloaded to this folder.

   We assume you have used the direct download of the New Analytics data (and not filtered data which has different file patterns)
<br>

   c) Once run successfully and your new analytics files added, run the next script which will reorganize your files into project_data (this is needed to be anonymized next)
   > `$ python src/create_project_structure.py`

   You will now see a project_data folder with course_structure and user_data files organized. All user_data files are those with any user identifiers included. 

   ![image_of_env_file](img/step-b-folder-output.png)
<br>
   d) Now, if you need to anonymize your data, run the last script. This will copy all course_structure data, and make anonymized versions of user_data. It will also create a folder with data called project_data_anonymized_keys for if you need to pull all of the anonymized data back together. 
   > `$ python src/anonymize.py`

   ![image_of_env_file](img/step-d-folder-output.png)


## 🌟 Acknowledgements & Contributions
This project relies heavily on the [CanvasAPI](https://github.com/ucfopen/canvasapi) python library from The University of Central Florida's open source software projects - [UCF Open](https://ucfopen.github.io/).

### Contributers

[**Sauder Learning Services**](https://www.sauder.ubc.ca/about-ubc-sauder/learning-services/people)
- [Marko Prodanovic](https://github.com/markoprodanovic), Data Analyst & Media Specialist
- [Alison Myers](https://github.com/alisonmyers), Research Analyst