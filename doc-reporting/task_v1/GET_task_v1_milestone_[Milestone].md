
[Module](./README.md)

[Main page](../README.md)


# GET on task/v1/milestone/[Milestone]

## Description

https://api.groupcamp.com/task/v1/milestone/[Milestone]


Return the milestone.



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
Milestone | Uuid | Milestone UUID.









## Return value


This method returns a [Milestone](../types/Milestone.md) object.





## Errors


HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user.
404 | not_found |  | Requested element was not found for the current user.



