# Dictionaries - for data cleaning once downloaded (see transform_project_data.py)
ASSIGNMENTS_DICT = {
    "name": "assignments",
    "rename_dict": {    
            'id': 'assignment_id',
            'description': 'assignment_description',
            'due_at': 'assignment_due_at',
            'points_possible': 'assignment_points_possible',
            'name': 'assignment_title',
            'submission_types': 'assignment_submission_types',
            'workflow_state': 'assignment_workflow_state',
            'rubric': 'assignment_rubric',
            'is_quiz_assignment': 'assignment_is_quiz',
            'published': 'assignment_is_published',
            'course_id': 'course_id'
    }
}

FILES_DICT = {
    "name": "files",
    "rename_dict": {
            'id': 'file_id',
            'folder_id': 'file_folder_id',
            'display_name': 'file_display_title',
            'content-type': 'file_type',
            'created_at': 'file_created_at'
    }
}

DISCUSSIONTOPICS_DICT = {
    "name": "discussion_topics",
    "rename_dict": {
            'id': 'discussion_topic_id',
            'title': 'discussion_topic_title',
            'assignment_id': 'assignment_id',
            'discussion_type': 'discussion_type',
            'published': 'discussion_is_published',
            'course_id': 'course_id'
    }
}

MODULEITEMS_DICT = {
    "name": "module_items",
    "rename_dict": {
            'id': 'module_item_id',
            'title': 'module_item_title',
            'position': 'module_item_position',
            'type': 'module_item_type',
            'module_id': 'module_id',
            'html_url': 'module_item_html_url',
            'page_url': 'module_item_page_url',
            'url': 'module_item_url',
            'published': 'module_item_published',
            'course_id': 'course_id',
            'content_id': 'module_item_content_id'   
    }
}

MODULES_DICT = {
    "name": "modules",
    "rename_dict": {
            'id': 'module_id',
            'name': 'module_title',
            'position': 'module_position',
            'published': 'module_is_published',
            'course_id': 'course_id'
    }
}

PAGES_DICT = {
    "name": "pages",
    "rename_dict": {
            'page_id': 'page_id',
            'title': 'page_title',
            'published': 'page_is_published',
            'html_url': 'page_html_url',
            'course_id': 'course_id',
            'url': 'page_url'
    }
}

QUIZZES_DICT = {
    "name": "quizzes",
    "rename_dict": {
            'id': 'quiz_id',
            'title': 'quiz_title',
            'description': 'quiz_description',
            'quiz_type': 'quiz_type'
    }
}
    # NOTE - some changes necessary for not anon dataset!

ASSIGNMENTSUBMISSIONS_DICT = {
    "name": "assignment_submissions",
    "rename_dict": {
            'user_id': 'user_id',
            'id': 'assignment_submission_id',
            'score': 'assignment_score',
            'submitted_at': 'assignment_submitted_at',
            'submission_type': 'submission_type',
            'assignment_id': 'assignment_id',
            'workflow_state': 'assignment_submission_status',
            'attempt': 'assignment_attempt',
            'seconds_late': 'assignment_seconds_late',
            'course_id': 'course_id'
    }
}
    # NOTE - some changes necessary for not anon dataset!

ENROLLMENTS_DICT = {
    "name": "enrollments",
    "rename_dict": {
            'user_id': 'user_id',
            'course_id': 'course_id',
            'type': 'enrollment_type',
            'course_section_id': 'enrollment_course_section',
            'role': 'user_role',
            'enrollment_state': 'enrollment_state'
    }
}

    # NOTE - some changes necessary for not anon dataset!

NEWANALYTICS_DICT = {
    "name": "new_analytics",
    "rename_dict": {
            'globalStudentId': 'global_user_id',
            'globalCourseId': 'global_course_id',
            'contentType': 'content_type',
            'contentName': 'content_name',
            'pageviewCount': 'pageview_count',
            'participationCount': 'participation_count',
            'startDate': 'access_date',
            'lastAccessTime': 'last_access_datetime',
            'firstAccessTime': 'first_access_datetime',
            'file': 'original_data_file'
    }
}

GRADEBOOKUSERDATA_DICT = {
    "name": "gradebook_user_data",
    "rename_dict": {
        "ID": "canvas_user_id",
        "Current Points": "gb_current_points",
        "Final Points": "gb_final_points",
        "Current Score": "gb_current_score",
        "Final Score": "gb_final_score"
    }
}