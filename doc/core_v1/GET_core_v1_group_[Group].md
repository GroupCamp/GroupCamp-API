
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/group/[Group]

## Description


Return the group.



## Parameters in the URL

In the URL, here are the expected values

Name   | Type    | Description
-------|---------|------------
Group | Uuid | The UUID of a group









## Return value


This method returns a JSON structure. An anonymous generic object

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | The UUID of the group
name | String | The name of the group. Can contain the Project Code, if appropriate.
group_name | String | The raw group name. Without any Project Code
type | Const( = group ) | The type of the object
gtype | Enum(project, intranet, extranet) | The group's type
state | Enum(archi, ok, del, trash) | The current state of this group
description | String | The group's description
orga | [SimpleOrga](../types/SimpleOrga.md) | The organization to display, linked to this group
leader1 | [SimpleUser](../types/SimpleUser.md) | The project manager
leader2 | [SimpleUser](../types/SimpleUser.md) | The project manager's assistant
managing_team | [SimpleTeam](../types/SimpleTeam.md) | The management team of the project
category | [SimpleGcat](../types/SimpleGcat.md) | The category of the group
access | Enum(open, invited) | Group access status
description_color | Enum(default, green, orange, red) | The color to use for the description background
can_accept_guest | Boolean | If the group can accept guest members
nb_users | Integer | The number of users inside that group






## Possible errors


HTTP Starus | Name   | Optional detail   | Description  
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check ids in the URL path of your request.	
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user	
404 | not_found |  | Requested element was not found for the current user	


