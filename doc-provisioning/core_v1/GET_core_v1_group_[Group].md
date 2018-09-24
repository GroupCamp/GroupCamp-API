
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/group/[Group]

## Description

https://api.groupcamp.com/core/v1/group/[Group]


Return the group.



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
Group | Uuid | Group UUID.









## Return value





  
  This method returns a JSON structure. An anonymous generic object

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | Group UUID.
name | String | Group name. Can contain the Project Code, if applicable.
group_name | String | Raw group name, without Project Code.
type | Const( = group ) | Constant. Sert to 'group'.
gtype | Enum(project, intranet, extranet) | Group type.
state | Enum(archi, ok, del, trash) | Current group status.
description | String | Group description.
orga | [SimpleOrga](../types/SimpleOrga.md) | Client company associated to the group.
leader1 | [SimpleUser](../types/SimpleUser.md) | Project manager 1 of the group.
leader2 | [SimpleUser](../types/SimpleUser.md) | Project manager 2 (assistant) of the group.
managing_team | [SimpleTeam](../types/SimpleTeam.md) | Management team of the project.
category | [SimpleGcat](../types/SimpleGcat.md) | Group category.
access | Enum(open, invited) | Group access status.
users | Array([SimpleUser](../types/SimpleUser.md)) | An Array of SimpleUser objects. List of group members.
description_color | Enum(default, green, orange, red) | The color to use for the description background.
can_accept_guest | Boolean | True when the group can have guest members.
nb_users | Integer | Number of group members.
dates | Object | Project dates.
dates.start | Date | Project start date
dates.end | Date | Project end date
rich_tags | Array([STag](../types/STag.md)) | Group's tags
tags_names | Array(String) | Group's tags names

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.
404 | not_found |  | Requested item was not found for the current user.



