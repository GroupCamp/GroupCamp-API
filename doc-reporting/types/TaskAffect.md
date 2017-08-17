
[The known types](./README.md)

[Main page](../README.md)

# TaskAffect type definition

Name    |   Type  |  Description
--------|---------|-------------
user | Alternative([Nobody](../types/Nobody.md), [SimpleUser](../types/SimpleUser.md)) | Can be a SimpleUser object, or the Nobody object. Assigned user.
user.maybe[0] | [Nobody](../types/Nobody.md) | Alternative
user.maybe[1] | [SimpleUser](../types/SimpleUser.md) | Alternative
progress | Integer | Completion of the task for that assigned user (%).
estimate | [Duration](../types/Duration.md) | A Duration object. Estimated time for the assigned user.


