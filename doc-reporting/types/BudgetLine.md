
[The known types](./README.md)

[Main page](../README.md)

# BudgetLine type definition

Name    |   Type  |  Description
--------|---------|-------------
type | Enum(total, category, role, other) | The type of the line
role | String | The role for this line of budget, if the budget type is 'role'.
category | String | The category for this line of budget, if the budget type is 'category'.
work | Integer | The planned work on that line of the budget.
spent | Integer | The time spent (sum of the timelogs, actual work) on that line of the budget.
billable | Integer | The part of spent time which is flagged as billable.
unit_cost | Integer | The unit cost for this line of the budget, per unit of time. This field is an integer value in 1/1000th, so 1000 is 1.00 of your currency par unit of time (hour, or day).
cost | Integer | The planned cost for that line (the [unit_cost] field times the [time] field, scaled down according to the [time_unit]).
role_cost | Integer | The sum of timelogs cost, each timelog being evaluated at the cost of the role on the day of the timelog.
user_cost | Integer | The sum of timelogs cost, each timelog being evaluated at the cost of the user on the day of the timelog.


