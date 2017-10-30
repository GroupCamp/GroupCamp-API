
[Module](./README.md)

[Main page](../README.md)


# GET on task/v1/group/[Group]/tasks

## Description

https://api.groupcamp.com/task/v1/group/[Group]/tasks


Returns tasks owned by a group. When this method is called with inconsistent GET parameters, it returns an empty list.



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
Group | Uuid | Group UUID.





## GET parameters

Optional or required values.

Name    |  Mandatory    |   Multiple[1]    |   Type   |  Description
--------|---------------|------------------|----------|---------------
state | Optional | No | Enum(open, completed) | Only tasks having this state are returned. Requesting 'state=open' and a completion date ('cpl_begin' or 'cpl_end') is inconsistent and will return an empty list.
due_begin | Optional | No | Date | Only tasks having a due date, and with due date equal of after 'due_begin' will be returned. Due date can be inherited from a Milestone.
due_end | Optional | No | Date | Only tasks having a due date equal or before 'due_end' will be returned.
cpl_begin | Optional | No | Date | Only completed tasks, and with a completion date equal of after 'cpl_begin' will be returned. Tasks only partialy completed will not be returned.
cpl_end | Optional | No | Date | Only tasks having a completion date equal or before 'cpl_end' will be returned.
crea_begin | Optional | No | Date | Only tasks that have a creation date equal or after 'crea_begin' will be returned.
crea_end | Optional | No | Date | Only tasks that have a creation date equal or before 'crea_end' will be returned.
mod_begin | Optional | No | Date | Only tasks that have a last-modification date equal or after 'mod_begin' will be returned.
mod_end | Optional | No | Date | Only tasks that have a last-modification date equal or before 'mod_end' will be returned.


[1] Can the GET parameter be provided several times. If Yes, the
parameter can be provided several times, each value being used. If
No, a request with several values will be rejected.






## Return value



Results are paginated. See documentation on the [paging mechanism](../../Paging.md) for
more informations.

Mechanism used: `next`




  
  This method returns a JSON structure. An array, all items are of type [Task](../types/Task.md) 

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | Task UUID.
name | String | Task name.
description | String | Task description.
list | [TaskList](../types/TaskList.md) | A TaskList object. The task list of the task.
creation_date | DateTime | A DateTime object. Task creation date.
creator | [SimpleUser](../types/SimpleUser.md) | A SimpleUser object. User who created the task.
modification_date | DateTime | A DateTime object. Task modification date. 
completion_date | DateTime | A DateTime object. Task completion date.
completed_by | [SimpleUser](../types/SimpleUser.md) | A SimpleUser object. User who completed the task.
track_time | Object | Time spent records.
track_time.total | [Duration](../types/Duration.md) | Total of time spent records for that task (sum of every assigned user, as found in the TaskAffect objects, plus time spent for other users, not having the task assigned, plus time spent not assigned to any user).
is_open | Boolean | True for non-completed task.
affects | Array([TaskAffect](../types/TaskAffect.md)) | An Array of TaskAffect objects. Assigned users, or Nobody.
begin | Alternative(Object, Object) | Task start date. Can be an empty object when the task has no start date, or an object with a date.
begin.maybe[0] | Object | Alternative
begin.maybe[0].type | Const( = date ) | Constant. Set to 'date' when the task has a date.
begin.maybe[0].date | Date | Task date.
begin.maybe[1] | Object | Alternative
begin.maybe[1].type | Const( = empty ) | Constant. Set to 'empty' when the task has no date.
end | Alternative(Object, Object, Object) | Task end date. Can be an empty object when the task has no due date, an object with a date, or an object with the UUID of a milestone.
end.maybe[0] | Object | Alternative
end.maybe[0].type | Const( = date ) | Constant. Set to 'date' when the task has a date.
end.maybe[0].date | Date | Task date.
end.maybe[1] | Object | Alternative
end.maybe[1].type | Const( = milestone ) | Constant. Set to 'milestone' when the task has an end date which is the due date of a milestone.
end.maybe[1].date | Date | The due date of the related milestone.
end.maybe[1].id | Uuid | Milestone UUID. The milestone is linked to the TaskList where the task is.
end.maybe[2] | Object | Alternative
end.maybe[2].type | Const( = empty ) | Constant. Set to 'empty' when the task has no date.

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.
404 | not_found |  | Requested item was not found for the current user.



