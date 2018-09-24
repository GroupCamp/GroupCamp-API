
[The known types](./README.md)

[Main page](../README.md)

# SimpleOrga type definition

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | Organisation UUID.
name | String | Organisation name. As shown in the UI. May contain the names of the up-stream organisations.
type | Const( = orga ) | Constant. Must be 'orga'.
otype | Enum(internal, invited) | Organisation type.
state | Enum(ok, del) | Current organisation status.


