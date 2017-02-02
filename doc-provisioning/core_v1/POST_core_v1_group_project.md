
[Module](./README.md)

[Main page](../README.md)


# POST on core/v1/group/project

## Description


Creates a new group of type 'project'.







## Body of the request


This method requires a JSON object to be transmited in the body of the request.

Name   |  Type   |   Description
-------|---------|--------------
name | String | The name of the group to be created. Must be unique accross the groups in the same GroupCamp account.
external_ref | String | The external reference. Must be unique.
project_code | String | The project code. Must be unique. Set to an empty value to remove the existing code from a project.
description | String | The description of the group, can be left empty.
category_name | String | The name of the category for this project. Category MUST exist. Name is case-sentitive.
leader1 | Uuid | The UUID of the project-manager
leader2 | Uuid | The UUID of the deputy project-manager
managers | Array(Uuid) | The UUIDs of other additional project managers
management_team | Uuid | The UUID of the managing team if there is one for that project. The value 'none' instead of an UUID will remove the managing_team from an existing project.
access | Enum(invite, open) | Access control rule used for that group
with_guests | Boolean | Can users of type 'guest' be member of this group
template | Object | To use a group as a template
template.id | Uuid | The UUID of the group used as a template. It's settings will be copied.
template.members | Boolean | Copy the members of the template-group in the new group.
template.track | Boolean | Copy the budget and authorised time categories
template.topics | Boolean | Copy the topics of the 'discussion' application
template.files | Object | How to handle files (Files in the folder "Shared with the group" are ignored)
template.files.folders | Boolean | Copy the folders tree
template.files.owned | Boolean | Copy the files owned by the group (requires folders tree)
template.files.others | Boolean | Link into the new group the files listed in the template-group's folders, but not owned by it (requires folders tree)





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






## Possible errors


HTTP Starus | Name   | Optional detail   | Description  
------------|--------|-------------------|------------
400 | bad_request | error_body_data | Bad Request. Please check the request's body.	
400 | bad_request | error_json | Bad Request. Please check that the body of your request is a valid json object.	
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user	
403 | forbidden | over_group_quota | You have reach the group quota of your space	



