
[The known types](./README.md)

[Main page](../README.md)

# The definition of type TaskAffect

Name    |   Type  |  Description
--------|---------|-------------
user | Alternative([Nobody](../types/Nobody.md), [SimpleUser](../types/SimpleUser.md)) | The affected user
user.maybe[0] | [Nobody](../types/Nobody.md) | Alternative
user.maybe[1] | [SimpleUser](../types/SimpleUser.md) | Alternative
progress | Integer | The progress of the affect, : 0, 10, 20, 30, 40, 50, 60, 70, 80, 90 or 100
estimate | [Duration](../types/Duration.md) | The estimated time for that affected person


