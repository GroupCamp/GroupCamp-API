
[Module](./README.md)

[Main page](../README.md)


# GET on track/v1/timelogs

## Description

https://api.groupcamp.com/track/v1/timelogs


Returns all the time spent records matching the search criterions.





## GET parameters

Optional or required values.

Name    |  Mandatory    |   Type   |  Description
--------|---------------|----------|---------------
start | Mandatory | Date | Return time spent records after this date.
end | Mandatory | Date | Return time spent records before this date. The maximum date range allowed from start to end is 42 days (6 weeks).






## Return value


This method returns a JSON structure. An array, all elements are of type [Timelog](../types/Timelog.md) 

Name   |  Type   |  Description
-------|---------|-------------
id | Uuid | Time spent record UUID.
name | String | Record description.
date | Date | Record date.
user | Alternative([Nobody](../types/Nobody.md), [SimpleUser](../types/SimpleUser.md)) | Returns a SimpleUser object or the Nobody object. User who has spent time.
user.maybe[0] | [Nobody](../types/Nobody.md) | Alternative
user.maybe[1] | [SimpleUser](../types/SimpleUser.md) | Alternative
time_unit | Enum(s, d) | The default time_unit to use. Depends on the request you made. For example, on a user based request, it will be the time unit for the user. On a project based request, it will be the project time unit.
duration | [Duration](../types/Duration.md) | Time spent record duration.
creation_date | DateTime | Record  creation date.
modification_date | DateTime | Record update date.
modification_user | [SimpleUser](../types/SimpleUser.md) | User who last updated the record.
billable | Boolean | True when the time spent record is billable. Null if not applicable.
owner | Alternative([SimpleGroup](../types/SimpleGroup.md), [SimpleTimelogCategory](../types/SimpleTimelogCategory.md)) | Time spent record owner. Can be a group, or a time category (administrative time category). The Timelog app must be enabled in the group.
owner.maybe[0] | [SimpleGroup](../types/SimpleGroup.md) | Alternative
owner.maybe[1] | [SimpleTimelogCategory](../types/SimpleTimelogCategory.md) | Alternative
category | [SimpleTimelogCategory](../types/SimpleTimelogCategory.md) | Project time category. Only applicable if the owner is a group.
object | Alternative([Nothing](../types/Nothing.md), Object) | The object on which the time spent record has been recorded.
object.maybe[0] | [Nothing](../types/Nothing.md) | Alternative
object.maybe[1] | Object | Alternative
object.maybe[1].id | Uuid | Task UUID.
object.maybe[1].type | Const( = task ) | Constant. Object type. Set to 'task'.
object.maybe[1].appli | Const( = task ) | Constant. Application name. Set to 'task'.






## Errors


HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_body_data | Bad Request. Please check the request body.
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.
403 | forbidden | access_forbidden | The requested item cannot be accessed by the current user.
410 | gone | gone | This temporary item has gone away. You should start again to re-create the temporary item.



