# Python3 code to demonstrate working of
# Start week from year and weekday
# Using %W, %w
from datetime import datetime, timedelta

# initializing year
test_year = 1997

# initializing week
test_week = 27

# printing original date
print("The original year, week is : " + str(test_year) + " " + str(test_week))

date = str(test_year) + '-W' + str(test_week)

# getting date
res = datetime.strptime(date + '-1', "%Y-W%W-%w")

# printing result
print("The starting date of week : " + str(res))
