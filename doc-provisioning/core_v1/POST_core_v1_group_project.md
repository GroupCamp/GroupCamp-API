
[Module](./README.md)

[Main page](../README.md)


# POST on core/v1/group/project

## Description

https://api.groupcamp.com/core/v1/group/project


Creates a new group of type 'project'.







## Request body


This method requires a JSON object in the body of the request.

Name   |  Mandatory  |  Type   |   Description
-------|-------------|---------|--------------
name | Mandatory | String | Group name. Must be unique in the GroupCamp account.
external_ref | Optional | String | External unique reference. This is your app reference.
project_code | Optional | String | Project code. Must be unique. Set to an empty value to remove an existing Project code.
description | Optional | String | Group description.
category_name | Optional | String | Project group category. You must select an existing group category from your GroupCamp account. Group category is case-sensitive. A setting located in the GroupCamp Admin panel decides is the field is mandatory or not.
tags_names | Optional | Array(String) | The tags added to the project. Tags used here but are created if they do not yet exist. If an empty list is provided while editing a group, all the tags are removed. If no list is provided, tags are unchanged.
leader1 | Optional | Uuid | Project manager 1 UUID.
leader2 | Optional | Uuid | Project manager 2 UUID (assistant).
managers | Optional | Array(Uuid) | UUIDs of other additional project managers (must be employees, cannot be guests).
subtype | Optional | Enum(internal, customer) | Is this an internal project ?
orga | Optional | Uuid | Organisation UUID, mandatory if subtype is "customer"
access | Optional | Enum(invite, open) | Group access. Open to all colleagues or By invitation only.
with_guests | Optional | Boolean | True when the group can have guest members.
template | Optional | Object | To use a group as a template
template.id | Mandatory | Uuid | UUID of the group template. Settings of this group will be copied.
template.members | Optional | Boolean | Copy template gorup members to the new group.
template.track | Optional | Boolean | Copy budget and authorised time categories.
template.topics | Optional | Boolean | Set to true to copy topics from the 'Discussion' application.
template.files | Optional | Object | How to handle files (Files in the folder "Shared with the group" are ignored).
template.files.folders | Optional | Boolean | Set to true to copy folders tree from the 'Files' application.
template.files.owned | Optional | Boolean | Set to true to copy the files owned by the template group. Requires folders tree to be copied.
template.files.others | Optional | Boolean | Set to true to link the files not owned by the template group. Requires folders tree to be copied.





## Return value





  
  This method returns a JSON structure. An anonymous generic object

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | Group UUID.
name | String | Group name.
type | Const( = group ) | Constant. Must be 'group'.
gtype | Enum(project, intranet, extranet) | Type of group.
subtype | Enum(internal, customer) | Is this an internal project ?
orga | Uuid | The UUID of the customer's company, if the project's subtype is 'customer'
state | Enum(archi, ok, del, trash) | Current group status.
tags_names | Array(String) | The names on the tags which are on the group.
description | String | Group description.
starred | Integer | When the group is starred for current user, returns the index order of the group in the list of starred groups for current user.
can_accept_guest | Boolean | True when the group can have guest members.
nb_users | Integer | Number of group members.

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_body_data | Bad Request. Please check the request body.
400 | bad_request | error_json | Bad Request. Please check that the body of your request is a valid json object.
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.
403 | forbidden | over_group_quota | You have reached the quota of groups from your GroupCamp current plan.



