# Enrollments

> Last Reviewed: 2021-03-02
https://canvas.instructure.com/doc/api/enrollments.html


```json
An Enrollment Object

{
  // The ID of the enrollment.
  "id": 1,
  // The unique id of the course.
  "course_id": 1,
  // The SIS Course ID in which the enrollment is associated. Only displayed if
  // present. This field is only included if the user has permission to view SIS
  // information.
  "sis_course_id": "SHEL93921",
  // The Course Integration ID in which the enrollment is associated. This field
  // is only included if the user has permission to view SIS information.
  "course_integration_id": "SHEL93921",
  // The unique id of the user's section.
  "course_section_id": 1,
  // The Section Integration ID in which the enrollment is associated. This field
  // is only included if the user has permission to view SIS information.
  "section_integration_id": "SHEL93921",
  // The SIS Account ID in which the enrollment is associated. Only displayed if
  // present. This field is only included if the user has permission to view SIS
  // information.
  "sis_account_id": "SHEL93921",
  // The SIS Section ID in which the enrollment is associated. Only displayed if
  // present. This field is only included if the user has permission to view SIS
  // information.
  "sis_section_id": "SHEL93921",
  // The SIS User ID in which the enrollment is associated. Only displayed if
  // present. This field is only included if the user has permission to view SIS
  // information.
  "sis_user_id": "SHEL93921",
  // The state of the user's enrollment in the course.
  "enrollment_state": "active",
  // User can only access his or her own course section.
  "limit_privileges_to_course_section": true,
  // The unique identifier for the SIS import. This field is only included if the
  // user has permission to manage SIS information.
  "sis_import_id": 83,
  // The unique id of the user's account.
  "root_account_id": 1,
  // The enrollment type. One of 'StudentEnrollment', 'TeacherEnrollment',
  // 'TaEnrollment', 'DesignerEnrollment', 'ObserverEnrollment'.
  "type": "StudentEnrollment",
  // The unique id of the user.
  "user_id": 1,
  // The unique id of the associated user. Will be null unless type is
  // ObserverEnrollment.
  "associated_user_id": null,
  // The enrollment role, for course-level permissions. This field will match
  // `type` if the enrollment role has not been customized.
  "role": "StudentEnrollment",
  // The id of the enrollment role.
  "role_id": 1,
  // The created time of the enrollment, in ISO8601 format.
  "created_at": "2012-04-18T23:08:51Z",
  // The updated time of the enrollment, in ISO8601 format.
  "updated_at": "2012-04-18T23:08:51Z",
  // The start time of the enrollment, in ISO8601 format.
  "start_at": "2012-04-18T23:08:51Z",
  // The end time of the enrollment, in ISO8601 format.
  "end_at": "2012-04-18T23:08:51Z",
  // The last activity time of the user for the enrollment, in ISO8601 format.
  "last_activity_at": "2012-04-18T23:08:51Z",
  // The last attended date of the user for the enrollment in a course, in ISO8601
  // format.
  "last_attended_at": "2012-04-18T23:08:51Z",
  // The total activity time of the user for the enrollment, in seconds.
  "total_activity_time": 260,
  // The URL to the Canvas web UI page for this course enrollment.
  "html_url": "https://...",
  // The URL to the Canvas web UI page containing the grades associated with this
  // enrollment.
  "grades": {"html_url":"https:\/\/...","current_score":35,"current_grade":null,"final_score":6.67,"final_grade":null},
  // A description of the user.
  "user": {"id":3,"name":"Student 1","sortable_name":"1, Student","short_name":"Stud 1"},
  // The user's override grade for the course.
  "override_grade": "A",
  // The user's override score for the course.
  "override_score": 99.99,
  // The user's current grade in the class including muted/unposted assignments.
  // Only included if user has permissions to view this grade, typically teachers,
  // TAs, and admins.
  "unposted_current_grade": "",
  // The user's final grade for the class including muted/unposted assignments.
  // Only included if user has permissions to view this grade, typically teachers,
  // TAs, and admins..
  "unposted_final_grade": "",
  // The user's current score in the class including muted/unposted assignments.
  // Only included if user has permissions to view this score, typically teachers,
  // TAs, and admins..
  "unposted_current_score": "",
  // The user's final score for the class including muted/unposted assignments.
  // Only included if user has permissions to view this score, typically teachers,
  // TAs, and admins..
  "unposted_final_score": "",
  // optional: Indicates whether the course the enrollment belongs to has grading
  // periods set up. (applies only to student enrollments, and only available in
  // course endpoints)
  "has_grading_periods": true,
  // optional: Indicates whether the course the enrollment belongs to has the
  // Display Totals for 'All Grading Periods' feature enabled. (applies only to
  // student enrollments, and only available in course endpoints)
  "totals_for_all_grading_periods_option": true,
  // optional: The name of the currently active grading period, if one exists. If
  // the course the enrollment belongs to does not have grading periods, or if no
  // currently active grading period exists, the value will be null. (applies only
  // to student enrollments, and only available in course endpoints)
  "current_grading_period_title": "Fall Grading Period",
  // optional: The id of the currently active grading period, if one exists. If
  // the course the enrollment belongs to does not have grading periods, or if no
  // currently active grading period exists, the value will be null. (applies only
  // to student enrollments, and only available in course endpoints)
  "current_grading_period_id": 5,
  // The user's override grade for the current grading period.
  "current_period_override_grade": "A",
  // The user's override score for the current grading period.
  "current_period_override_score": 99.99,
  // optional: The student's score in the course for the current grading period,
  // including muted/unposted assignments. Only included if user has permission to
  // view this score, typically teachers, TAs, and admins. If the course the
  // enrollment belongs to does not have grading periods, or if no currently
  // active grading period exists, the value will be null. (applies only to
  // student enrollments, and only available in course endpoints)
  "current_period_unposted_current_score": 95.8,
  // optional: The student's score in the course for the current grading period,
  // including muted/unposted assignments and including ungraded assignments with
  // a score of 0. Only included if user has permission to view this score,
  // typically teachers, TAs, and admins. If the course the enrollment belongs to
  // does not have grading periods, or if no currently active grading period
  // exists, the value will be null. (applies only to student enrollments, and
  // only available in course endpoints)
  "current_period_unposted_final_score": 85.25,
  // optional: The letter grade equivalent of
  // current_period_unposted_current_score, if available. Only included if user
  // has permission to view this grade, typically teachers, TAs, and admins. If
  // the course the enrollment belongs to does not have grading periods, or if no
  // currently active grading period exists, the value will be null. (applies only
  // to student enrollments, and only available in course endpoints)
  "current_period_unposted_current_grade": "A",
  // optional: The letter grade equivalent of current_period_unposted_final_score,
  // if available. Only included if user has permission to view this grade,
  // typically teachers, TAs, and admins. If the course the enrollment belongs to
  // does not have grading periods, or if no currently active grading period
  // exists, the value will be null. (applies only to student enrollments, and
  // only available in course endpoints)
  "current_period_unposted_final_grade": "B"
}
```
## Data

_requester
id
user_id
course_id
type
created_at
created_at_date
updated_at
updated_at_date
associated_user_id
start_at
end_at
course_section_id
root_account_id
limit_privileges_to_course_section
enrollment_state
role
role_id
last_activity_at
last_activity_at_date
last_attended_at
total_activity_time
grades
sis_account_id
sis_course_id
course_integration_id
sis_section_id
section_integration_id
sis_user_id
html_url
user