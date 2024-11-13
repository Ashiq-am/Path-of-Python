# Python3 code to demonstrate working of
# Get Last date of Month
# Using calendar()
from datetime import datetime
import calendar

# initializing date
test_date = datetime(2018, 6, 4)

# printing original date
print("The original date is : " + str(test_date))

# monthrange() gets the date range
# required of month
res = calendar.monthrange(test_date.year, test_date.month)[1]

# printing result
print("Last date of month : " + str(res))
