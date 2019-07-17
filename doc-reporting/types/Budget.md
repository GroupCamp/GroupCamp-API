
[The known types](./README.md)

[Main page](../README.md)

# Budget type definition

Name    |   Type  |  Description
--------|---------|-------------
group_id | Uuid | Group UUID
type | Enum(total, category, role) | The type of budget
time_unit | Enum(s, d) | The time_unit of the budget
work | Integer | The planned work of the budget (in seconds, if [time_unit] is hours, in 1/1000 of a day, if [time_unit] is days). It is the sum of the time in each relevant line of the budget.
currency | String | The currency, if there is a budget amount.
amount | Integer | The budget amount (in thousanth, so 1000 = 1.00 of your currency)
description | String | Description
lines | Array([BudgetLine](../types/BudgetLine.md)) | The content of the budget. If type is 'global', only one line of type 'global'. If the type is 'role' or 'category', one line per budgted role, plus lines for the other categories and roles. If the sum of timelogs are required, there will be one line of type 'other' for each category or role with spent time which is not part of the planned budget.


