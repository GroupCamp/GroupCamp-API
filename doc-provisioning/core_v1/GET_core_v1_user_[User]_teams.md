
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/user/[User]/teams

## Description

https://api.groupcamp.com/core/v1/user/[User]/teams


Returns the list of all teams having this user as a member



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
User | Uuid | The UUID of a user









## Return value


This method returns a JSON structure. An array, all elements are of type Object 

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | Team UUID.
name | String | Team name.
type | Const( = team ) | Constant, must be 'team'.
state | Enum(ok) | Team status. There is no trash for teams, they are deleted immediately.
description | String | Team description.
is_tech | Boolean | True when the team is a Management team.






## Errors


HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user.
404 | not_found |  | Requested element was not found for the current user.



