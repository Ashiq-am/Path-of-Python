# Python3 code to demonstrate working of
# Next weekday from Date
# Using timedelta() + weekday()
import datetime

# initializing dates
test_date = datetime.datetime(2017, 3, 14)

# printing original date
print("The original date is : " + str(test_date)[:10])

# initializing weekday index
weekday_idx = 4

# computing delta days
days_delta = weekday_idx - test_date.weekday()
if days_delta <= 0:
	days_delta += 7

# adding days to required result
res = test_date + datetime.timedelta(days_delta)

# printing result
print("Next date of required weekday : " + str(res)[:10])
