# GroupCamp API

You'll find here some pieces of code showing how to use the
GroupCamp public provisioning and reporting APIs.

## Manifest:

* group.py shows, based on standard Python libraries, how to create
  a project and add users in that project.
* track.py shows how to fetch time-logs from the GroupCamp
  application
* task.py shows how to fetch informations about some elements in
  the reporting API (typicaly a task related to a time-log entry)

## Interfaces:

* [Provisioning](doc-provisioning/README.md) is the API to create elements
  in your GroupCamp account (create projects, add users in projects, etc)
* [Reporting](doc-reporting/README.md) is the API to get some reports from
  your GroupCamp account (get timelogs and related informations)


