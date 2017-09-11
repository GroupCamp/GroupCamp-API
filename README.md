# GroupCamp REST API

You'll find here some pieces of code showing how to use the
GroupCamp public provisioning and reporting REST APIs.

To enable APIs accesses in your GroupCamp account, please consult
this page: https://www.groupcamp.com/h/introduction-groupcamp-api

## Manifest:

* group.py shows, based on standard Python libraries, how to create
  a project and add users in that project.
* track.py shows how to fetch timei spent records from the GroupCamp
  account
* task.py shows how to fetch informations about items with 
  the reporting API (typicaly when a time spent record is attached
  to as task)

## Interfaces:

* The [Provisioning](doc-provisioning/README.md) API allows to create items
  in your GroupCamp account (create projects, add users in projects, etc)
* The [Reporting](doc-reporting/README.md) is the API to get some reports from
  your GroupCamp account (get tasks, task lists, milestones, spent time records,
  and related informations)


