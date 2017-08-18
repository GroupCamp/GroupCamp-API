
[The known types](./README.md)

[Main page](../README.md)

# TaskList type definition

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | TaskList UUID.
name | String | TaskList name.
group | [SimpleGroup](../types/SimpleGroup.md) | A SimpleGroup object. Group owner.
description | String | TaskList description.
milestone | Alternative([Nothing](../types/Nothing.md), [Milestone](../types/Milestone.md)) | Can be an Empty object, or a Milestone, when the task list is linked with a milestone.
milestone.maybe[0] | [Nothing](../types/Nothing.md) | Alternative
milestone.maybe[1] | [Milestone](../types/Milestone.md) | Alternative
is_private | Boolean | True when the task-list is private.
is_closed | Boolean | True when the task-list is completed (all tasks in the list are completed).


