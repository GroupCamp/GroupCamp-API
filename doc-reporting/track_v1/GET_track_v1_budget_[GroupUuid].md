
[Module](./README.md)

[Main page](../README.md)


# GET on track/v1/budget/[GroupUuid]

## Description

https://api.groupcamp.com/track/v1/budget/[GroupUuid]


Returns the current budget for the projet, if there is a valid budget available.



## URL parameters

Expected values

Name   | Type    | Description
-------|---------|------------
GroupUuid | Uuid | The UUID of the project





## GET parameters

Optional or required values.

Name    |  Mandatory    |   Multiple[1]    |   Type   |  Description
--------|---------------|------------------|----------|---------------
with_detail | Optional | No | Integer | Include each line of the budget in the result.
with_spent | Optional | No | Integer | Include informations about the time spent in the budget, and in each line of the budget.


[1] Can the GET parameter be provided several times. If Yes, the
parameter can be provided several times, each value being used. If
No, a request with several values will be rejected.






## Return value





  
  This method returns a [Budget](../types/Budget.md) object.
  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
400 | bad_request | error_id | Bad Request. Please check IDs in the URL path of your request.
400 | bad_request | get_parameter_error | At least one of the GET parameters is wrong or missing.
403 | forbidden | invalid_budget | Something is wrong about the budget of that project. May happen if the currency on your GroupCamp account has changed since the budget was saved, or if the time unit have been changed, or if the project dates and the budget dates are different.
403 | forbidden | wrong_gtype | The GroupUUID you provided is the one of a group which is not suitable for your request.
404 | not_found |  | Requested item was not found for the current user.



