
[The known types](./README.md)

[Main page](../README.md)

# The definition of type Timelog

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | The UUID of time log
name | String | The description of the time log
date | Date | The date of the time log
user | Alternative([Nobody](../types/Nobody.md), [SimpleUser](../types/SimpleUser.md)) | The user affected to the time log
time_unit | Enum(s, d) | The default time_unit to use. Depends on the request you made. For example, on a user based request, it will be the time unit for the user. On a project based request, it will be the project time unit.
duration | [Duration](../types/Duration.md) | The time spent
creation_date | DateTime | The creation date of the time log
modification_date | DateTime | The modification date of the time log
modification_user | [SimpleUser](../types/SimpleUser.md) | The user who modified the time log
billable | Boolean | If the time log is billable. Null if not applicable
owner | Alternative([SimpleGroup](../types/SimpleGroup.md), [SimpleTimelogCategory](../types/SimpleTimelogCategory.md)) | The owner of the time log. Can be a group, or a time log category. If it is a group, the group must have the time log application enabled.
category | [SimpleTimelogCategory](../types/SimpleTimelogCategory.md) | Only applicable if the owner is a project group. The project category for the time log.


