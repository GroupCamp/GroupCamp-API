# About durations, cost and computations

## Duration

When the time unit is **day** in your GroupCamp account, all the related
durations in the API (in timelogs, in budgets, in reports, etc) are expressed
as intergers, which are 1/1000 of a day. So a value of 500 is half-a-day,
and a value of 1000 is a day.

When the time unit is **hour** in your GroupCamp account, all the related
durations in the API (in timelogs, in budgets, in reports, etc) are expressed
as integers, which are a number of seconds. So a value of 1800 is hal-an-hour,
and a value of 7200 is 2 hours.

## Amounts

Whatever the currency of your account, amounts are always expressed as integers
which are 1/1000 of a unit of your currency. So if the currency is USD, a value
of 1500 is $1.50, and if the currency is EUR, a value of 5200 is 5.20 euros.

## Unit cost and cost

When a unit cost is expressed, it is in 1/1000 of currency per time unit.

So if time unit is **day**, and currency is USD, a value of 125000 means
a unit cost of $125.00 per day.

And if time unit is **hour**, and currency is EUR, a value of 25000 means
a unit cost of 25.00 euros per hour.

## Example in hours

`duration` = 7200

`unit_cost` = 35000

`currency` = EUR

The cost will be ( 35000 ) * ( 7200 / 3600 ) = 70000, which is a cost
of 70.00 euros for a duration of 2 hours.

## Example in days

`duration` = 4500

`unit_cost` = 240000

`currency` = USD

The cost will be ( 240000 ) * ( 4500 / 1000 ) = 1080000, which is a cost
of $1.080,00 for a duraton of 4.5 days.


