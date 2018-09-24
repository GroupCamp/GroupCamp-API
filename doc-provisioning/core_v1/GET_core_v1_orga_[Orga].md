
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/orga/[Orga]

## Description

https://api.groupcamp.com/core/v1/orga/[Orga]


Return the organisation.



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
Orga | Uuid | A (sub-)organization UUID.









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
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.
404 | not_found |  | Requested item was not found for the current user.



