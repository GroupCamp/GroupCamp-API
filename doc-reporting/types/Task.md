
[The known types](./README.md)

[Main page](../README.md)

# The definition of type Task

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
begin | Alternative(Object, Object) | The beginning date of the task
begin.maybe[0] | Object | Alternative
begin.maybe[0].type | Const( = date ) | The type of the echeance
begin.maybe[0].date | Date | The date of the echeance
begin.maybe[1] | Object | Alternative
begin.maybe[1].type | Const( = empty ) | The type of the echeance
end | Alternative(Object, Object, Object) | The end date of the task
end.maybe[0] | Object | Alternative
end.maybe[0].type | Const( = date ) | The type of the echeance
end.maybe[0].date | Date | The date of the echeance
end.maybe[1] | Object | Alternative
end.maybe[1].type | Const( = milestone ) | The type of the echeance
end.maybe[1].date | Date | The date of the echeance
end.maybe[1].id | Uuid | The milestone the echeance is linked to
end.maybe[2] | Object | Alternative
end.maybe[2].type | Const( = empty ) | The type of the echeance


