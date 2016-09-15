
[The known types](./README.md)

[Main page](../README.md)

# The definition of type SimpleTeam

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | UUID of the team
name | String | The name of the team, as if should be shown on the interface
type | Const( = team ) | Constant, must be 'team'
state | Enum(ok) | The current state of this team, there is no trash for teams, they are deleted immediately
is_management | Boolean | True if the team is a management team


