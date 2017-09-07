
[Module](./README.md)

[Main page](../README.md)


# GET on task/v1/tasks

## Description

https://api.groupcamp.com/task/v1/tasks


Return tasks matching the filters.





## GET parameters

Optional or required values.

Name    |  Mandatory    |   Multiple[1]    |   Type   |  Description
--------|---------------|------------------|----------|---------------
group | Optional | Yes | Uuid | Only tasks owned by and of those groups will be returned.
list | Optional | No | Uuid | Task list where to search tasks. If the 'group' parameter is provided in an inconstent way (without the group owner of the task list), an empty result will be returned without a warning. It is safer to omit the 'group' parameter.
to | Optional | Yes | Uuid | Tasks assigned to any of those users are returned.


[1] Can the GET parameter be provided several times. If yes, the
parameter can be provided several times, each value being used. If
no, a request with several values will be rejected.






## Return value



The results are paginated. See documentation on the [pagin mechanism](../../Paging.md) for
more informations.

Mechanism used: `next`




  
  This method returns a JSON structure. An array, all elements are of type [Task](../types/Task.md) 

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | Task UUID.
name | String | Task name.
description | String | Task description.
list | [TaskList](../types/TaskList.md) | A TaskList object. The task list of the task.
creation_date | DateTime | A DateTime object. Task creation date.
creator | [SimpleUser](../types/SimpleUser.md) | A SimpleUser object. User who created the task.
completion_date | DateTime | A DateTime object. Completion creation date.
completed_by | [SimpleUser](../types/SimpleUser.md) | A SimpleUser object. User who completed the task.
track_time | Object | Time spent records.
track_time.total | [Duration](../types/Duration.md) | Total of time spent records for that task (sum of every assigned user, as found in the TaskAffect objects, plus time for other users, not having the task assigned, plus time not assigned to any user).
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
end.maybe[1].type | Const( = milestone ) | Constant. Set to 'milestone' when the task has an end date which is the due date of a milesonte.
end.maybe[1].date | Date | The due date of the related milestone.
end.maybe[1].id | Uuid | Milestone UUID. The milestone is linked to the TaskList where the task is.
end.maybe[2] | Object | Alternative
end.maybe[2].type | Const( = empty ) | Constant. Set to 'empty' when the task has no date.

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)
* `Gone`, see documentation about [paging mechanism](../../Paging.md)


Specific errors this method may return:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.
404 | not_found |  | Requested item was not found for the current user.



