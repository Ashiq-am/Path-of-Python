# Python3 code to demonstrate working of
# Business days in range
# Using timedelta() + sum() + weekday()
from datetime import datetime, timedelta

# initializing dates ranges
test_date1, test_date2 = datetime(2015, 6, 3), datetime(2015, 7, 1)

# printing dates
print("The original range : " + str(test_date1) + " " + str(test_date2))

# generating dates
dates = (test_date1 + timedelta(idx + 1)
		for idx in range((test_date2 - test_date1).days))

# summing all weekdays
res = sum(1 for day in dates if day.weekday() < 5)

# printing
print("Total business days in range : " + str(res))
