
[Module](./README.md)

[Main page](../README.md)


# GET on task/v1/task_list/[TaskList]

## Description


Return the task-list.



## Parameters in the URL

In the URL, here are the expected values

Name   | Type    | Description
-------|---------|------------
TaskList | Uuid | The UUID of a task list









## Return value


This method returns an object of type [TaskList](../types/TaskList.md).





## Possible errors


HTTP Starus | Name   | Optional detail   | Description  
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check ids in the URL path of your request.	
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user	
404 | not_found |  | Requested element was not found for the current user	



