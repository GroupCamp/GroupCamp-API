
[Module](./README.md)

[Main page](../README.md)


# GET on track/v1/report

## Description

https://api.groupcamp.com/track/v1/report


Returns the current global report for the projets selected according to the GET parameters.





## GET parameters

Optional or required values.

Name    |  Mandatory    |   Multiple[1]    |   Type   |  Description
--------|---------------|------------------|----------|---------------
name | Optional | No | String | Any group having exactly this name will be returned.
search | Optional | No | String | Groups where the string matches the group name will be returned.
user | Optional | No | Uuid | Groups were the user is a member will be returned.
leader | Optional | No | Uuid | Groups were this user is a leader will be returned.
managing | Optional | No | Uuid | Groups were this user is a leader or a managing member will be returned.
tag_name | Optional | Yes | String | Only groups having all of the cited tags are returned. If an empty string is provided as a tag name, only groups with no tags are returned. Providing at the same time an empty string *and* a normal string will search for groups having, at the same time, no tag (the empty string) and the regular tag. Result will then be empty.
project_type | Optional | No | Enum(internal, customer) | Only project groups will be returned, and only if their project_type is matching.
state | Optional | Yes | Enum(all, ok, archi, del, trash) | When the filter is not set, only group with the 'ok' status will be returned. When the filter is set, only groups with the given status will be returned.


[1] Can the GET parameter be provided several times. If Yes, the
parameter can be provided several times, each value being used. If
No, a request with several values will be rejected.






## Return value





  
  This method returns a JSON structure. An array, all items are of type [ProjectReport](../types/ProjectReport.md) 

Name   |  Type   |  Description
-------|---------|-------------
project | [ProjectInReport](../types/ProjectInReport.md) | Informations about the project
budget | [BudgetInReport](../types/BudgetInReport.md) | Informations about the budget, if there is a budget for that project.
budget_missing | Enum(no_budget, invalid) | Reason why the budget is missing
time_indates | [TimeInReport](../types/TimeInReport.md) | Informations about the time spent on the project, only the timelogs between the start-date and the end-date of the project are taken.
time_total | [TimeInReport](../types/TimeInReport.md) | Informations about the time spent on the project, even before the start-date or after the end-date. The times in time_total should be identical to the ones in time_indates, or more.

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.



