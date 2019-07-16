
[The known types](./README.md)

[Main page](../README.md)

# Budget type definition

Name    |   Type  |  Description
--------|---------|-------------
group_id | Uuid | Group UUID
type | Enum(total, category, role) | The type of budget
time_unit | Enum(s, d) | The time_unit of the budget
time | Integer | The total amount of the budget in time (in seconds, if time_unit is hours, in 1/1000 of a day, if time_unit is days). It is the sum of the time in each relevant line of the budget.
amount | Integer | The total amount of the budget in money (in thousanth, so 1000 = 1.00)
currency | String | The currency, if there is a budget in money.
description | String | Description
lines | Array([BudgetLine](../types/BudgetLine.md)) | The content of the budget. If type is 'global', only one line of type 'global'. If the type is 'role', one line per budgted role plus one for the time spend outside of the budgeted roles. If the type is 'category', one line per budgeted categpry plus one for the time spent outside of the budgeted categories.


