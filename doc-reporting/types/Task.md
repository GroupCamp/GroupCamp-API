
[The known types](./README.md)

[Main page](../README.md)

# Task type definition

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | Task UUID.
name | String | Task name.
description | String | Task description.
list | [TaskList](../types/TaskList.md) | A TaskList object. The task list of the task.
creation_date | DateTime | A DateTime object. Task creation date.
creator | [SimpleUser](../types/SimpleUser.md) | A SimpleUser object. User who created the task.
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


