
[Module](./README.md)

[Main page](../README.md)


# POST on core/v1/orga/invited

## Description

https://api.groupcamp.com/core/v1/orga/invited


Creates an invited organisation







## Request body


This method requires a JSON object in the body of the request.

Name   |  Mandatory  |  Type   |   Description
-------|-------------|---------|--------------
name | Mandatory | String | The name of the new invited organisation. Must be unique across all invited organisations. If an organisation by that name already exists, and is compatible with the request, it is returned with a successful status.
description | Optional | String | A description of the organisation.





## Return value





  
  This method returns a JSON structure. An anonymous generic object

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | UUID of the organisation
name | String | The name of the organisation. May contain the names of the parent organisations (for internal organisations).
type | Const( = orga ) | Constant, must be 'orga'
otype | Enum(internal, invited) | The organisation's type.
state | Enum(ok, del) | The organisation's current state.
description | String | The organisation's description
website | String | Organisation's Web site
creation_date | DateTime | Organisation's creation date and time
modification_date | DateTime | Organisation's last modification date and time

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_body_data | Bad Request. Please check the request body.
400 | bad_request | error_json | Bad Request. Please check that the body of your request is a valid json object.
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.



