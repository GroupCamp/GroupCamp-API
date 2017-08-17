
[The known types](./README.md)

[Main page](../README.md)

# Task type definition

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | The UUID of the task
name | String | The name of the task
description | String | The description of the task
list | [TaskList](../types/TaskList.md) | The task-list of the task
creation_date | DateTime | The creation date of the task
creator | [SimpleUser](../types/SimpleUser.md) | The creator of the task
is_open | Boolean | True if the task is not finished
affects | Array([TaskAffect](../types/TaskAffect.md)) | The list of affects
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


