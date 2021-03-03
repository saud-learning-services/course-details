# External Tools

Nothing returned in test course (10456)

> Last Reviewed: 2021-03-02
https://canvas.instructure.com/doc/api/external_tools.html


```
No Object Listed...

API for accessing and configuring external tools on accounts and courses. "External tools" are IMS LTI links: http://www.imsglobal.org/developers/LTI/index.cfm

NOTE: Placements not documented here should be considered beta features and are not officially supported.

Returns the specified external tool.

API response field:
id
The unique identifier for the tool

domain
The domain to match links against

url
The url to match links against

consumer_key
The consumer key used by the tool (The associated shared secret is not returned)

name
The name of the tool

description
A description of the tool

created_at
Timestamp of creation

updated_at
Timestamp of last update

privacy_level
What information to send to the external tool, “anonymous”, “name_only”, “public”

custom_fields
Custom fields that will be sent to the tool consumer

is_rce_favorite
Boolean determining whether this tool should be in a preferred location in the RCE.

account_navigation
The configuration for account navigation links (see create API for values)

assignment_selection
The configuration for assignment selection links (see create API for values)

course_home_sub_navigation
The configuration for course home navigation links (see create API for values)

course_navigation
The configuration for course navigation links (see create API for values)

editor_button
The configuration for a WYSIWYG editor button (see create API for values)

homework_submission
The configuration for homework submission selection (see create API for values)

link_selection
The configuration for link selection (see create API for values)

migration_selection
The configuration for migration selection (see create API for values)

resource_selection
The configuration for a resource selector in modules (see create API for values)

tool_configuration
The configuration for a tool configuration link (see create API for values)

user_navigation
The configuration for user navigation links (see create API for values)

selection_width
The pixel width of the iFrame that the tool will be rendered in

selection_height
The pixel height of the iFrame that the tool will be rendered in

icon_url
The url for the tool icon

not_selectable
whether the tool is not selectable from assignment and modules
```
## Data
