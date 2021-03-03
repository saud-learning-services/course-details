# Assignments

> Last Reviewed: 2021-03-02
https://canvas.instructure.com/doc/api/assignments.html

```json
An AssignmentObject
// Object representing a due date for an assignment or quiz. If the due date
// came from an assignment override, it will have an 'id' field.
{
  // (Optional, missing if 'base' is present) id of the assignment override this
  // date represents
  "id": 1,
  // (Optional, present if 'id' is missing) whether this date represents the
  // assignment's or quiz's default due date
  "base": true,
  "title": "Summer Session",
  // The due date for the assignment. Must be between the unlock date and the lock
  // date if there are lock dates
  "due_at": "2013-08-28T23:59:00-06:00",
  // The unlock date for the assignment. Must be before the due date if there is a
  // due date.
  "unlock_at": "2013-08-01T00:00:00-06:00",
  // The lock date for the assignment. Must be after the due date if there is a
  // due date.
  "lock_at": "2013-08-31T23:59:00-06:00"
}
```

## Data
_requester
id
description
due_at
unlock_at
lock_at
points_possible
grading_type
assignment_group_id
grading_standard_id
created_at
created_at_date
updated_at
updated_at_date
peer_reviews
automatic_peer_reviews
position
grade_group_students_individually
anonymous_peer_reviews
group_category_id
post_to_sis
moderated_grading
omit_from_final_grade
intra_group_peer_reviews
anonymous_instructor_annotations
anonymous_grading
graders_anonymous_to_graders
grader_count
grader_comments_visible_to_graders
final_grader_id
grader_names_visible_to_final_grader
allowed_attempts
secure_params
course_id
name
submission_types
has_submitted_submissions
due_date_required
max_name_length
in_closed_grading_period
is_quiz_assignment
can_duplicate
original_course_id
original_assignment_id
original_assignment_name
original_quiz_id
workflow_state
muted
html_url
has_overrides
needs_grading_count
sis_assignment_id
integration_id
integration_data
published
unpublishable
only_visible_to_overrides
locked_for_user
submissions_download_url
post_manually
anonymize_students
require_lockdown_browser
due_at_date
quiz_id
anonymous_submissions
use_rubric_for_grading
free_form_criterion_comments
rubric
rubric_settings
is_quiz_lti_assignment
frozen_attributes
external_tool_tag_attributes
url
lock_at_date
unlock_at_date
peer_review_count
peer_reviews_assign_at