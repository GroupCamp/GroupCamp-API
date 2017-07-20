
[The known types](./README.md)

[Main page](../README.md)

# The definition of type Milestone

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | The UUID of the milestone
name | String | The name of the milestone
group | [SimpleGroup](../types/SimpleGroup.md) | The group where the milestone is
description | String | The description of the milestone
is_private | Boolean | True if the milsetone is private
is_open | Boolean | True if the milestone is not completed
date | Date | The date of the milestone
user | Alternative([Nobody](../types/Nobody.md), [SimpleUser](../types/SimpleUser.md)) | The person responsible of that milestone
user.maybe[0] | [Nobody](../types/Nobody.md) | Alternative
user.maybe[1] | [SimpleUser](../types/SimpleUser.md) | Alternative


