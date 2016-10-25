
[The known types](./README.md)

[Main page](../README.md)

# The definition of type SimpleOrga

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | UUID of the organization
name | String | The name of the organization, as it should be shown on the interface. May contain the names of the up-stream organizations.
type | Const( = orga ) | Constant, must be 'orga'
otype | Enum(internal, invited) | The organization's type.
state | Enum(ok, del) | The organization's current state.
picture | [Picture](../types/Picture.md) | The organization's picture


