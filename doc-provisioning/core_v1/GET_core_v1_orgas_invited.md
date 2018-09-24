
[Module](./README.md)

[Main page](../README.md)


# GET on core/v1/orgas/invited

## Description

https://api.groupcamp.com/core/v1/orgas/invited


List all the invited organisations









## Return value





  
  This method returns a JSON structure. An array, all items are of type [SimpleOrga](../types/SimpleOrga.md) 

Name   |  Type   |  Description
-------|---------|-------------
 | [SimpleOrga](../types/SimpleOrga.md) | Each item of the Array

  





## Errors

Generic errors may be sent by every method:
* `unauthorized`, see documentation about [authentication](../../Auth.md)


This method can return specific errors:

HTTP Status | Name   | Optional          | Description
------------|--------|-------------------|------------
403 | forbidden | access_forbidden | Requested item cannot be retrieved by the current user.



