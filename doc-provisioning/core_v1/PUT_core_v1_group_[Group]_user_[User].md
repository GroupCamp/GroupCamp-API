
[Module](./README.md)

[Main page](../README.md)


# PUT on core/v1/group/[Group]/user/[User]

## Description


Adds a user as member in a group



## Parameters in the URL

In the URL, here are the expected values

Name   | Type    | Description
-------|---------|------------
Group | Uuid | The UUID of a group
User | Uuid | The UUID of a user









## Return value


This method returns a JSON structure. An anonymous generic object

Name   |  Type   |  Description
-------|---------|-------------
value | Const( = ok ) | The response if everything went well






## Possible errors


HTTP Starus | Name   | Optional detail   | Description  
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check ids in the URL path of your request.	
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user	
404 | not_found |  | Requested element was not found for the current user	



