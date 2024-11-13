# Python3 code to demonstrate working of
# Business days in range
# Using pd.bdate_range
from datetime import datetime
import pandas as pd

# initializing dates ranges
test_date1, test_date2 = datetime(2015, 6, 3), datetime(2015, 6, 30)

# printing dates
print("The original range : " + str(test_date1) + " " + str(test_date2))

# generating total days using pd.bdate_range()
# len() gets the number of days
# includes both last and first date.
res = len(pd.bdate_range(test_date1.strftime('%Y-%m-%d'),
						test_date2.strftime('%Y-%m-%d')))

# printing result
print("Total business days in range : " + str(res))
