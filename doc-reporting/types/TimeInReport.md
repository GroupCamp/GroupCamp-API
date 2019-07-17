
[The known types](./README.md)

[Main page](../README.md)

# TimeInReport type definition

Name    |   Type  |  Description
--------|---------|-------------
time_unit | Enum(s, d) | The time_unit
total_time | Integer | The total time spent on the project. In seconds, if `time_unit` is "s", or in 1/1000 of a day if `time_unit` is "d".
billable_time | Integer | The part of the total time spent which is flagged as being billable. Can be 0.
user_cost | Integer | The total cost of the time spent, computed from the cost of each user at the time of the timelog. In 1/1000 of the usual currency of the GroupCamp account.
role_cost | Integer | The total cost of the time spent, computed from the cost of earch role at the time of the timelog. In 1/1000 of the usual currency of the GroupCamp account.


