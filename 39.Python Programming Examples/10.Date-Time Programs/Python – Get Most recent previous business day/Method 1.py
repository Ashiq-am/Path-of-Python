# Python3 code to demonstrate working of
# Last business day
# using timedelta() + conditional statements + weekday()
from datetime import datetime, timedelta

# initializing dates
test_date = datetime(2020, 1, 31)

# printing original date
print("The original date is : " + str(test_date))

# getting difference
diff = 1
if test_date.weekday() == 0:
    diff = 3
elif test_date.weekday() == 6:
    diff = 2
else:
    diff = 1

# subtracting diff
res = test_date - timedelta(days=diff)

# printing result
print("Last business day : " + str(res))
