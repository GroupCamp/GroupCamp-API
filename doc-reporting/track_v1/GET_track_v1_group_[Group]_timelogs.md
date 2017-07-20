
[Module](./README.md)

[Main page](../README.md)


# GET on track/v1/group/[Group]/timelogs

## Description


Returns timelogs in the target group



## Parameters in the URL

In the URL, here are the expected values

Name   | Type    | Description
-------|---------|------------
Group | Uuid | The UUID of a group





## Parameters in GET

Here are the possible/expected query parameters.

Name    |  Type   |  Description 
--------|---------|--------------
start | Date | Return timelogs after this date
end | Date | Return timelogs before this date






## Return value


This method returns a JSON structure. An array, all elements are of type [Timelog](../types/Timelog.md) 

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | The UUID of time log
name | String | The description of the time log
date | Date | The date of the time log
user | Alternative([Nobody](../types/Nobody.md), [SimpleUser](../types/SimpleUser.md)) | The user affected to the time log
user.maybe[0] | [Nobody](../types/Nobody.md) | Alternative
user.maybe[1] | [SimpleUser](../types/SimpleUser.md) | Alternative
time_unit | Enum(s, d) | The default time_unit to use. Depends on the request you made. For example, on a user based request, it will be the time unit for the user. On a project based request, it will be the project time unit.
duration | [Duration](../types/Duration.md) | The time spent
creation_date | DateTime | The creation date of the time log
modification_date | DateTime | The modification date of the time log
modification_user | [SimpleUser](../types/SimpleUser.md) | The user who modified the time log
billable | Boolean | If the time log is billable. Null if not applicable
owner | Alternative([SimpleGroup](../types/SimpleGroup.md), [SimpleTimelogCategory](../types/SimpleTimelogCategory.md)) | The owner of the time log. Can be a group, or a time log category. If it is a group, the group must have the time log application enabled.
owner.maybe[0] | [SimpleGroup](../types/SimpleGroup.md) | Alternative
owner.maybe[1] | [SimpleTimelogCategory](../types/SimpleTimelogCategory.md) | Alternative
category | [SimpleTimelogCategory](../types/SimpleTimelogCategory.md) | Only applicable if the owner is a project group. The project category for the time log.
object | Alternative([Nothing](../types/Nothing.md), Object) | The object on which the timelog is assigned
object.maybe[0] | [Nothing](../types/Nothing.md) | Alternative
object.maybe[1] | Object | Alternative
object.maybe[1].id | Uuid | UUID of a task
object.maybe[1].type | Const( = task ) | Object type
object.maybe[1].appli | Const( = task ) | Object application






## Possible errors


HTTP Starus | Name   | Optional detail   | Description  
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check ids in the URL path of your request.	
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing	
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user	
410 | gone | gone | This temporary item have gone away. You should start again to create the temporary item again.	



