
[The known types](./README.md)

[Main page](../README.md)

# BudgetLine type definition

Name    |   Type  |  Description
--------|---------|-------------
type | Enum(total, category, role, other) | The type of the line. It is the same as the `type` of the budget, except for line of type `other` which are about off budget informations when the budget type is either `role` or `category`.
role | String | The role for this line of budget, if the budget type is `role`.
category | String | The category for this line of budget, if the budget type is `category`.
work | Integer | The planned work on that line of the budget (in seconds, if the budget `time_unit` is hours, in 1/1000 of a day if the budget `time_unit` is days).
spent | Integer | The time spent (sum of the timelogs, actual work) on that line of the budget.
billable | Integer | The part of time spent which is flagged as billable.
unit_cost | Integer | The unit cost for this line of the budget, per unit of time. This field is an integer value in 1/1000th, so 1000 is 1.00 of your currency per unit of time (one hour, or one day).
`work` = 3600, `time_unit` = s, `unit_cost` = 125000, currency = EUR -> leads to cost = 125000 (cost of 125.00 EUR for that line with 1 hour of planned work).
`work` = 3600, `time_unit` = d, `unit_cost` = 125000, currency = EUR -> leads to cost = 450000 (cost of 450.00 EUR for that line with 3.6 days of planned work).
cost | Integer | The planned cost for that line (the 'unit_cost` field times the `work` field, scaled down according to the `time_unit` as in the example above).
role_cost | Integer | The sum of timelogs cost, each timelog being evaluated at the cost of the role on the day of the timelog.
user_cost | Integer | The sum of timelogs cost, each timelog being evaluated at the cost of the user on the day of the timelog.


