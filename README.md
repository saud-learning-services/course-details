
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
- external tools
- features
- discussion_topics
- modules
- module_items
- files

### Course Details
- page links *TODO*
- quiz details *TODO*
- assignment details *TODO*
### Student Details
- student discussion responses *TODO*
- student quiz submissions *TODO*
- student assignment submissions *TODO*


![shows relationship between scope](img/simple_project_scope.png)

## 🚀 Use
### Computer Setup

1. We use conda, and suggest miniconda for your projects: [Install Miniconda](https://docs.conda.io/en/latest/miniconda.html) -> whichever the latest 3.x version is, use the 'pkg' version if you are unfamiliar with bash
2. We also like VSCode: [Install VSCode](https://code.visualstudio.com)
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
1. Make sure you have set `your_course_id` in the .env file
2. Create a new token and add it to API_TOKEN in .env

![image of how to get a token](img/create_a_token.png)

> i.e `API_TOKEN = 'some string here'`

3. Run the script
In terminal:
   i. Make sure you are in the right directory (if you opened the folder in vscode and see the project files in the explorer, then you are in the right directory) - check with the command:
   > `$ pwd`
   
   ii. Activate the environment
   > `$ conda activate canvas-get-course-details`
   
   iii. Run the script! (In terminal:)
   > `$ python src/get_course_data.py` 

## 🌟 Acknowledgements & Contributions
This project relies heavily on the [CanvasAPI](https://github.com/ucfopen/canvasapi) python library from [The University of Central Florida's](https://ucfopen.github.io/) open software project - UCF Open.

### Contributers

[**Sauder Learning Services**](https://www.sauder.ubc.ca/about-ubc-sauder/learning-services/people)
- [Marko Prodanovic](https://github.com/markoprodanovic), Data Analyst & Media Specialist
- [Alison Myers](https://github.com/alisonmyers), Research Analyst