
[Module](./README.md)

[Main page](../README.md)


# POST on core/v1/group/project/[Group]

## Description


Modifies a group of type 'project'.







## Body of the request


This method requires a JSON object to be transmited in the body of the request.

Name   |  Type   |   Description
-------|---------|--------------
name | String | The name of the group to be created. Must be unique accross the groups in the same GroupCamp account.
external_ref | String | The external reference. Must be unique.
description | String | The description of the group, can be left empty.
category_name | String | The name of the category for this project. Category MUST exist. Name is case-sentitive.
management_team | Uuid | The UUID of the managing team if there is one for that project.
access | Enum(invite, open) | Access control rule used for that group
with_guests | Boolean | Can users of type 'guest' be member of this group





## Return value


This method returns a JSON structure. An anonymous generic object

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | The UUID of the group
name | String | The name of the group
type | Const( = group ) | The type of the object
gtype | Enum(project, intranet, extranet) | The group's type
state | Enum(archi, ok, del, trash) | The current state of this group
description | String | The group's description
starred | Integer | If the group is starred for current user, the order of it
can_accept_guest | Boolean | If the group can accept guest members
nb_users | Integer | The number of users inside that group






## Possible errors


HTTP Starus | Name   | Optional detail   | Description  
------------|--------|-------------------|------------
400 | bad_request | error_body_data | Bad Request. Please check the request's body.	
400 | bad_request | error_id | Bad Request. Please check ids in the URL path of your request.	
400 | bad_request | error_json | Bad Request. Please check that the body of your request is a valid json object.	
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user	



