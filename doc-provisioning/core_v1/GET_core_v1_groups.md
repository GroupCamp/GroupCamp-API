
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/groups

## Description

https://api.groupcamp.com/core/v1/groups


Get groups matching search criterias. When criterias are incompatible, the search will return an empty list without warnings.





## GET parameters

Optional or required values.

Name    |  Mandatory    |   Multiple[1]    |   Type   |  Description
--------|---------------|------------------|----------|---------------
gtype | Optional | Yes | Enum(project, intranet, extranet) | Type of group.
name | Optional | No | String | Any group having exactly this name will be returned.
search | Optional | No | String | Groups where the string matches the group name will be returned.
user | Optional | No | Uuid | Groups were the user is a member will be returned.
category_name | Optional | No | String | Groups in that group category will be returned. Category name is case sensitive.
project_type | Optional | No | Enum(internal, customer) | Only project groups will be returned, and only if their project_type is matching.
state | Optional | Yes | Enum(all, ok, archi, del, trash) | When the filter is not set, only group with the 'ok' status will be returned. When the filter is set, only groups with the given status will be returned.


[1] Can the GET parameter be provided several times. If yes, the
parameter can be provided several times, each value being used. If
no, a request with several values will be rejected.






## Return value





  
  This method returns a JSON structure. An array, all elements are of type [SimpleGroup](../types/SimpleGroup.md) 

Name   |  Type   |  Description
-------|---------|-------------
 | [SimpleGroup](../types/SimpleGroup.md) | Each element of the Array

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


Specific errors this method may return:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.



