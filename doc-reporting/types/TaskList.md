
[The known types](./README.md)

[Main page](../README.md)

# The definition of type TaskList

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | The UUID of the task-list
name | String | The name of the task-list
group | [SimpleGroup](../types/SimpleGroup.md) | The group where the task-list is
description | String | The description of the task-list
milestone | Alternative([Nothing](../types/Nothing.md), [Milestone](../types/Milestone.md)) | If the task-list is linked to a milestone, that milestone (if the linked milestone is private then the privacy is forced on the task list)
milestone.maybe[0] | [Nothing](../types/Nothing.md) | Alternative
milestone.maybe[1] | [Milestone](../types/Milestone.md) | Alternative
is_private | Boolean | True if the task-list is private
is_closed | Boolean | True if the task-list was closed


