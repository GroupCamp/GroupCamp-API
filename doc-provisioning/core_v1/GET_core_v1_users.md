
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/users

## Description


Return all the users of the account, filtered according to the GET arguments received.





## Parameters in GET

Here are the possible/expected query parameters.

Name    |  Type   |  Description 
--------|---------|--------------
state | String | Filter selected users on their state.
user_type | String | Filter selected users on the user type.
is_leader | [FilterGroupType](../search/FilterGroupType.md) | Only returns users who are leaders of that type of group






## Return value


This method returns a JSON structure. An array, all elements are of type <a href="../types/SimpleUser.html">SimpleUser</a> 

Name   |  Type   |  Description
-------|---------|-------------
 | [SimpleUser](../types/SimpleUser.md) | Each element of the Array






## Possible errors


HTTP Starus | Name   | Optional detail   | Description  
------------|--------|-------------------|------------
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing	



