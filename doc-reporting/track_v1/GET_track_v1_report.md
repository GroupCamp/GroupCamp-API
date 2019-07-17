
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
name | Optional | No | String | Any project having exactly this name will be returned.
search | Optional | No | String | Projects where the string matches the project name will be returned.
user | Optional | No | Uuid | Projects were the user is a member will be returned.
leader | Optional | No | Uuid | Projects were this user is a Project leader ([leader1] or [leader2]) will be returned.
managing | Optional | No | Uuid | Projects were this user is a leader ([leader1], [leader2] or member with delagation) will be returned.
tag_name | Optional | Yes | String | Only projects having all of the cited tags are returned. If an empty string is provided as a tag name, only projects with no tags are returned. Providing at the same time an empty string *and* a normal string will search for groups having, at the same time, no tag (the empty string) and the regular tag. Resulting list of projects will then be empty.
project_type | Optional | No | Enum(internal, customer) | Only projects having this project_type are returned.


[1] Can the GET parameter be provided several times. If Yes, the
parameter can be provided several times, each value being used. If
No, a request with several values will be rejected.






## Return value





  
  This method returns a JSON structure. An array, all items are of type [ProjectReport](../types/ProjectReport.md) 

Name   |  Type   |  Description
-------|---------|-------------
project | [ProjectInReport](../types/ProjectInReport.md) | Informations about the project
budget | [BudgetInReport](../types/BudgetInReport.md) | Informations about the budget, if there is a budget for that project.
budget_missing | Enum(no_budget, invalid) | Reason why the budget is missing.
time_indates | [TimeInReport](../types/TimeInReport.md) | Informations about the time spent on the project, only the timelogs between the start-date and the end-date of the project are taken.
time_total | [TimeInReport](../types/TimeInReport.md) | Informations about the time spent on the project, even before the start-date or after the end-date. The times in time_total should be identical to the ones in time_indates, or larger.

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.



