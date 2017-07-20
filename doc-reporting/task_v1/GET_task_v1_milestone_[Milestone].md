
[Module](./README.md)

[Main page](../README.md)


# GET on task/v1/milestone/[Milestone]

## Description


Return the milestone.



## Parameters in the URL

In the URL, here are the expected values

Name   | Type    | Description
-------|---------|------------
Milestone | Uuid | The UUID of a milestone









## Return value


This method returns an object of type [Milestone](../types/Milestone.md).





## Possible errors


HTTP Starus | Name   | Optional detail   | Description  
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check ids in the URL path of your request.	
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user	
404 | not_found |  | Requested element was not found for the current user	



