
[Module](./README.md)

[Main page](../README.md)


# GET on task/v1/task/[Task]

## Description

https://api.groupcamp.com/task/v1/task/[Task]


Return the task.



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
Task | Uuid | Task UUID.









## Return value


This method returns a [Task](../types/Task.md) object.





## Errors


HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.
404 | not_found |  | Requested item was not found for the current user.



