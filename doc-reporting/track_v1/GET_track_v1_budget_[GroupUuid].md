
[Module](./README.md)

[Main page](../README.md)


# GET on track/v1/budget/[GroupUuid]

## Description

https://api.groupcamp.com/track/v1/budget/[GroupUuid]


Returns the current budget for the projet, if there is a valid budget available.



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
GroupUuid | Uuid | The UUID of the project









## Return value





  
  This method returns a [Budget](../types/Budget.md) object.
  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
403 | forbidden | wrong_gtype | The GroupUUID you provided is the one of a group which is not suitable for your request.
404 | not_found |  | Requested item was not found for the current user.



