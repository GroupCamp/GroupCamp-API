
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/groups

## Description

https://api.groupcamp.com/core/v1/groups


Get groups matching search criterias. When criterias are incompatible, the search will return an empty list without warnings.





## GET parameters

Optional or required values.

Name    |  Mandatory    |   Type   |  Description
--------|---------------|----------|---------------
gtype | Optional | Enum(project, intranet, extranet) | Type of group.
name | Optional | String | Any group having exactly this name will be returned.
search | Optional | String | Groups where the string matches the group name will be returned.
user | Optional | Uuid | Groups were the user is a member will be returned.
category_name | Optional | String | Groups in that group category will be returned. Category name is case sensitive.
project_type | Optional | Enum(internal, customer) | Only project groups will be returned, and only if their project_type is matching.
state | Optional | Enum(all, ok, archi, del, trash) | When the filter is not set, only group with the 'ok' status will be returned. When the filter is set, only groups with the given status will be returned.






## Return value


This method returns a JSON structure. An array, all elements are of type [SimpleGroup](../types/SimpleGroup.md) 

Name   |  Type   |  Description
-------|---------|-------------
 | [SimpleGroup](../types/SimpleGroup.md) | Each element of the Array






## Errors


HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.



