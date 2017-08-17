
[The known types](./README.md)

[Main page](../README.md)

# SimpleOrga type definition

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | Organization UUID.
name | String | Organization name. As shown in the UI. May contain the names of the up-stream organizations.
type | Const( = orga ) | Constant. Must be 'orga'.
otype | Enum(internal, invited) | Type of organization.
state | Enum(ok, del) | Current organization status.
picture | [Picture](../types/Picture.md) | Picture of the organization.


