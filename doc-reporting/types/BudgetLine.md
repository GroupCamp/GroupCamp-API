
[The known types](./README.md)

[Main page](../README.md)

# BudgetLine type definition

Name    |   Type  |  Description
--------|---------|-------------
type | Enum(total, category, role, other) | The type of the line
time | Integer | The amount of time on that line of the budget
spent | Integer | The amout of time spent (summ of the timelogs) on that line of the budget
unit_cost | Integer | The unit cost of this line of the budget, per unit of time. This field is an integer value in 1/1000th (1000 is 1 of your currency par unit of time).
cost | Integer | The budget cost for that line (the [unit_cost] field times the [time] field.
role_cost | Integer | The sum of the spent timelogs cost, each timelog being evaluated at the cost of the role on the day of the timelog.
user_cost | Integer | The sum of the spent timelogs cost, each timelog being evaluated at the cost of the user on the day of the timelog.


