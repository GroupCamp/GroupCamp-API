
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/groups

## Description


Returns informations about the groups matching the search criteria provided in the GET arguments. Incompatible search criterias will return an empty list without a warning.





## Parameters in GET

Here are the possible/expected query parameters.

Name    |  Type   |  Description 
--------|---------|--------------
gtype | Enum(project, intranet, extranet) | The type of group
name | String | Any group having exactly this name will be returned
search | String | Any group which have this text in its name will be returned
user | Uuid | Only groups which have this user among its members will be returned
category_name | String | Only group in a category having exactly this name will be returned
project_type | Enum(internal, customer) | Only project will be returned, and only if their project_type is matching
state | Enum(all, ok, archi, del, trash) | Only groups in the given state will be returned. If this filter is not provided, only groups in the state 'ok' are returned, thus to get all the groups, a filter set on 'all' is required






## Return value


This method returns a JSON structure. An array, all elements are of type <a href="../types/SimpleGroup.html">SimpleGroup</a> 

Name   |  Type   |  Description
-------|---------|-------------
 | [SimpleGroup](../types/SimpleGroup.md) | Each element of the Array






## Possible errors


HTTP Starus | Name   | Optional detail   | Description  
------------|--------|-------------------|------------
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing	



