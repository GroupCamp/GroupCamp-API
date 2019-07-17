
[The known types](./README.md)

[Main page](../README.md)

# ProjectReport type definition

Name    |   Type  |  Description
--------|---------|-------------
project | [ProjectInReport](../types/ProjectInReport.md) | Informations about the project
budget | [BudgetInReport](../types/BudgetInReport.md) | Informations about the budget, if there is a budget for that project.
budget_missing | Enum(no_budget, invalid) | Reason why the budget is missing.
time_indates | [TimeInReport](../types/TimeInReport.md) | Informations about the time spent on the project, only the timelogs between the start-date and the end-date of the project are taken.
time_total | [TimeInReport](../types/TimeInReport.md) | Informations about the time spent on the project, even before the start-date or after the end-date. The times in `time_total` should be identical to the ones in `time_indates`, or larger.


