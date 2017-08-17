
[The known types](./README.md)

[Main page](../README.md)

# SimpleTeam type definition

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | Team UUID.
name | String | Team name. As shown in the UI.
type | Const( = team ) | Constant. Must be 'team'.
state | Enum(ok) | Current team status. There is no trash for teams, teams are deleted immediately.
is_management | Boolean | True if the team is a management team.


