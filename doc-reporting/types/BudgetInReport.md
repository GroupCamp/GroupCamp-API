
[The known types](./README.md)

[Main page](../README.md)

# BudgetInReport type definition

Name    |   Type  |  Description
--------|---------|-------------
type | Enum(total, category, role) | The type of budget
time_unit | Enum(s, d) | The time_unit of the budget
work | Integer | The total planned work of the budget (in seconds, if time_unit is hours, in 1/1000 of a day, if time_unit is days). It is the sum of the time in each relevant line of the budget.
currency | String | The currency, if there is a total amount or unit costs for that budget.
amount | Integer | The total amount of the budget (in thousanth, so 1000 = 1.00 of your [currency])


