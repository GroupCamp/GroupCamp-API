
[The known types](./README.md)

[Main page](../README.md)

# SimpleGroup type definition

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | Group UUID.
name | String | Group name. As shown in the UI.
type | Const( = group ) | Constant. Must be 'group'.
gtype | Enum(project, intranet, extranet) | Type of group.
state | Enum(archi, ok, del, trash) | Current group status.


