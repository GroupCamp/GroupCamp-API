
[The known types](./README.md)

[Main page](../README.md)

# The definition of type SimpleUser

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | UUID of the user
name | String | The name of the user, as it should be shown on the interface
type | Const( = user ) | Constant, must be 'user'
utype | Enum(employee, guest) | The user's type
state | Enum(ok, del, trash) | The current state of this user


