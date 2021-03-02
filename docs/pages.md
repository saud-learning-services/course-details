# Pages

> Last Reviewed: 2021-03-02
https://canvas.instructure.com/doc/api/pages.html

```json
A Page Object
{
  // the unique locator for the page
  "url": "my-page-title",
  // the title of the page
  "title": "My Page Title",
  // the creation date for the page
  "created_at": "2012-08-06T16:46:33-06:00",
  // the date the page was last updated
  "updated_at": "2012-08-08T14:25:20-06:00",
  // (DEPRECATED) whether this page is hidden from students (note: this is always
  // reflected as the inverse of the published value)
  "hide_from_students": false,
  // roles allowed to edit the page; comma-separated list comprising a combination
  // of 'teachers', 'students', 'members', and/or 'public' if not supplied, course
  // defaults are used
  "editing_roles": "teachers,students",
  // the User who last edited the page (this may not be present if the page was
  // imported from another system)
  "last_edited_by": null,
  // the page content, in HTML (present when requesting a single page; omitted
  // when listing pages)
  "body": "<p>Page Content</p>",
  // whether the page is published (true) or draft state (false).
  "published": true,
  // whether this page is the front page for the wiki
  "front_page": false,
  // Whether or not this is locked for the user.
  "locked_for_user": false,
  // (Optional) Information for the user about the lock. Present when
  // locked_for_user is true.
  "lock_info": null,
  // (Optional) An explanation of why this is locked for the user. Present when
  // locked_for_user is true.
  "lock_explanation": "This page is locked until September 1 at 12:00am"
}
```
## Data
_requester
title
created_at
created_at_date
url
editing_roles
page_id
last_edited_by
published
hide_from_students
front_page
html_url
todo_date
updated_at
updated_at_date
locked_for_user
course_id
assignment



##