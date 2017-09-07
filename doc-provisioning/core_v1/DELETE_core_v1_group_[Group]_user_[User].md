
[Module](./README.md)

[Main page](../README.md)


# DELETE on core/v1/group/[Group]/user/[User]

## Description

https://api.groupcamp.com/core/v1/group/[Group]/user/[User]


Removes a user from a group



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
Group | Uuid | Group UUID.
User | Uuid | User UUID, or User e-mail address.









## Return value





  
  This method returns a JSON structure. An anonymous generic object

Name   |  Type   |  Description
-------|---------|-------------
value | Const( = ok ) | Constant. Value is 'ok'. Is returned when the requested action(s) has been performed successfully.

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


Specific errors this method may return:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.
404 | not_found |  | Requested item was not found for the current user.



