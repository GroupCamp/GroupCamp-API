
[The known types](./README.md)

[Main page](../README.md)

# Milestone type definition

Name    |   Type  |  Description
--------|---------|-------------
id | Uuid | Milestone UUID.
name | String | Milestone name.
group | [SimpleGroup](../types/SimpleGroup.md) | Group owner. A SimpleGroup object.
description | String | Milestone description.
is_private | Boolean | True when the milsetone is private.
is_open | Boolean | True if the milestone is open (not completed).
date | Date | Milestone date.
user | Alternative([Nobody](../types/Nobody.md), [SimpleUser](../types/SimpleUser.md)) | A SimpleUser object or the Nobody object. Milestone owner (assigned user).
user.maybe[0] | [Nobody](../types/Nobody.md) | Alternative
user.maybe[1] | [SimpleUser](../types/SimpleUser.md) | Alternative


