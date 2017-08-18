
[The known types](./README.md)

[Main page](../README.md)

# SimpleUser type definition

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | User UUID.
name | String | User name. As shown in the UI.
type | Const( = user ) | Constant. Must be 'user'.
utype | Enum(employee, guest) | Type of user.
state | Enum(ok, del, trash) | Current user status.


