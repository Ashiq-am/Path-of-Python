# Python3 code to demonstrate working of
# Business days in range
# Using np.busday_count
from datetime import datetime, timedelta
import numpy as np

# initializing dates ranges
test_date1, test_date2 = datetime(2015, 6, 3), datetime(2015, 7, 1)

# printing dates
print("The original range : " + str(test_date1) + " " + str(test_date2))

# generating total days using busday_count()
res = np.busday_count(test_date1.strftime('%Y-%m-%d'),
					test_date2.strftime('%Y-%m-%d'))

# printing
print("Total business days in range : " + str(res))
