
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/users

## Description

https://api.groupcamp.com/core/v1/users


Return all the users of the account, filtered according to the GET arguments received.





## GET parameters

Optional or required values.

Name    |  Mandatory    |   Multiple[1]    |   Type   |  Description
--------|---------------|------------------|----------|---------------
state | Optional | No | String | Filter selected users on their state.
user_type | Optional | No | String | Filter selected users on the user type.
is_leader | Optional | No | [FilterGroupType](../search/FilterGroupType.md) | Only returns users who are leaders of that type of group.


[1] Can the GET parameter be provided several times. If Yes, the
parameter can be provided several times, each value being used. If
No, a request with several values will be rejected.






## Return value





  
  This method returns a JSON structure. An array, all items are of type [SimpleUser](../types/SimpleUser.md) 

Name   |  Type   |  Description
-------|---------|-------------
 | [SimpleUser](../types/SimpleUser.md) | Each item of the Array

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.



