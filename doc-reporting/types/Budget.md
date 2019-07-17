
[The known types](./README.md)

[Main page](../README.md)

# Budget type definition

Name    |   Type  |  Description
--------|---------|-------------
group_id | Uuid | Group UUID
type | Enum(total, category, role) | The type of budget
time_unit | Enum(s, d) | The time_unit of the budget
work | Integer | The planned work of the budget (in seconds, if `time_unit` is hours, in 1/1000 of a day, if `time_unit` is days). It is the sum of the time in each relevant line of the budget.
currency | String | The currency, if there is a budget amount.
amount | Integer | The budget amount (in thousanth, so 1000 = 1.00 of your currency)
dates | [Dates](../types/Dates.md) | Budgt dates.
description | String | Description
lines | Array([BudgetLine](../types/BudgetLine.md)) | The content of the budget. If type is 'total', only one line of type 'total'. If the type is 'role' or 'category', one line per role/category in the budget (which type will be 'role' or 'category'), plus additional line(s) for the off budget informations. The type of those additional lines is 'other'. If the time spent is requested, there will be one line of type 'other' for each category or role with time spent which is off budget. If the time spent is not required only one line of type 'other' will be issued, which will contain the unit_cost for the off budget records.


