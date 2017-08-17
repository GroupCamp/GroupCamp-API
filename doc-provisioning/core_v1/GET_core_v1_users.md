
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/users

## Description

https://api.groupcamp.com/core/v1/users


Return all the users of the account, filtered according to the GET arguments received.





## GET parameters

Optional or required values.

Name    |  Mandatory    |   Type   |  Description 
--------|---------------|----------|---------------
state | Optional | String | Filter selected users on their state.
user_type | Optional | String | Filter selected users on the user type.
is_leader | Optional | [FilterGroupType](../search/FilterGroupType.md) | Only returns users who are leaders of that type of group






## Return value


This method returns a JSON structure. An array, all elements are of type [SimpleUser](../types/SimpleUser.md) 

Name   |  Type   |  Description
-------|---------|-------------
 | [SimpleUser](../types/SimpleUser.md) | Each element of the Array






## Errors


HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.



