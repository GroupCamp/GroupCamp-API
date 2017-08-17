
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/groups

## Description

https://api.groupcamp.com/core/v1/groups


Returns informations about the groups matching the search criteria provided in the GET arguments. Incompatible search criterias will return an empty list without a warning.





## GET parameters

Optional or required values.

Name    |  Mandatory    |   Type   |  Description 
--------|---------------|----------|---------------
gtype | Optional | Enum(project, intranet, extranet) | The type of group
name | Optional | String | Any group having exactly this name will be returned
search | Optional | String | Any group which have this text in its name will be returned
user | Optional | Uuid | Only groups which have this user among its members will be returned
category_name | Optional | String | Only group in a category having exactly this name will be returned
project_type | Optional | Enum(internal, customer) | Only project will be returned, and only if their project_type is matching
state | Optional | Enum(all, ok, archi, del, trash) | Only groups in the given state will be returned. If this filter is not provided, only groups in the state 'ok' are returned, thus to get all the groups, a filter set on 'all' is required






## Return value


This method returns a JSON structure. An array, all elements are of type [SimpleGroup](../types/SimpleGroup.md) 

Name   |  Type   |  Description
-------|---------|-------------
 | [SimpleGroup](../types/SimpleGroup.md) | Each element of the Array






## Errors


HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.



