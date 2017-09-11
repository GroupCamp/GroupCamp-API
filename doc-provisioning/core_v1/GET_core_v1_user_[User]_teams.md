
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/user/[User]/teams

## Description

https://api.groupcamp.com/core/v1/user/[User]/teams


Get a list of teams which have a user as a member.



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
User | Uuid | User UUID, or User e-mail address.









## Return value





  
  This method returns a JSON structure. An array, all items are of type Object 

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | Team UUID.
name | String | Team name.
type | Const( = team ) | Constant, must be 'team'.
state | Enum(ok) | Current team status. Value is 'ok'.
description | String | Team description.
is_tech | Boolean | True when the team is a management team.

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.
404 | not_found |  | Requested item was not found for the current user.



