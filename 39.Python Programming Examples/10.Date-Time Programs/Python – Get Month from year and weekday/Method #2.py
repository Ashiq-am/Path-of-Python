# Python3 code to demonstrate working of
# Start week from year and weekday
# Using relativedelta()
import datetime
from dateutil.relativedelta import relativedelta

# initializing year
test_year = 1997

# initializing week
test_week = 27

# printing original date
print("The original year, week is : " + str(test_year) + " " + str(test_week))

# contructing date
date = datetime.date(test_year, 1, 1)

# getting date by adding weeks to year beg.
# prints 9 July. as 1 jan was wednesday, 27th
# weeks beginning is from wed.
res = date + relativedelta(weeks=+test_week)

# printing result
print("The starting date of week : " + str(res))
