
[The known types](./README.md)

[Main page](../README.md)

# The definition of type SimpleGroup

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | UUID of the group
name | String | The name of the group, as it should be shown on the interface
type | Const( = group ) | Constant, must be 'group'
gtype | Enum(project, intranet, extranet) | The group's type
state | Enum(archi, ok, del, trash) | The current state of this group


