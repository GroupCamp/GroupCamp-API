
[Module](./README.md)

[Main page](../README.md)


# GET on task/v1/task_list/[TaskList]

## Description

https://api.groupcamp.com/task/v1/task_list/[TaskList]


Return the task-list.



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
TaskList | Uuid | TaskList UUID.









## Return value





  
  This method returns a [TaskList](../types/TaskList.md) object.
  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


Specific errors this method may return:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.
404 | not_found |  | Requested item was not found for the current user.



