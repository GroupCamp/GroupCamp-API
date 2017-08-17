
[Module](./README.md)

[Main page](../README.md)


# POST on core/v1/group/project/[Group]

## Description

https://api.groupcamp.com/core/v1/group/project/[Group]


Modifies a group of type 'project'.







## Request body


This method requires a JSON object to be transmited in the body of the request.

Name   |  Mandatory  |  Type   |   Description
-------|-------------|---------|--------------
name | Optional | String | The name of the group to be created. Must be unique accross the groups in the same GroupCamp account.
external_ref | Optional | String | The external reference. Must be unique.
project_code | Optional | String | The project code. Must be unique. Set to an empty value to remove the existing code from a project.
description | Optional | String | The description of the group, can be left empty.
category_name | Optional | String | The name of the category for this project. Category MUST exist. Name is case-sentitive.
leader1 | Optional | Uuid | The UUID of the project-manager
leader2 | Optional | Uuid | The UUID of the deputy project-manager
managers | Optional | Array(Uuid) | The UUIDs of other additional project managers
management_team | Optional | Uuid | The UUID of the managing team if there is one for that project. The value 'none' instead of an UUID will remove the managing_team from an existing project.
access | Optional | Enum(invite, open) | Access control rule used for that group
with_guests | Optional | Boolean | Can users of type 'guest' be member of this group





## Return value


This method returns a JSON structure. An anonymous generic object

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | The UUID of the group
name | String | The name of the group
type | Const( = group ) | The type of the object
gtype | Enum(project, intranet, extranet) | The group's type
state | Enum(archi, ok, del, trash) | The current state of this group
description | String | The group's description
starred | Integer | If the group is starred for current user, the order of it
can_accept_guest | Boolean | If the group can accept guest members
nb_users | Integer | The number of users inside that group






## Errors


HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_body_data | Bad Request. Please check the request body.
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
400 | bad_request | error_json | Bad Request. Please check that the body of your request is a valid json object.
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user.



