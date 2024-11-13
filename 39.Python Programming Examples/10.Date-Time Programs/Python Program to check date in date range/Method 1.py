# Python3 code to demonstrate working of
# Test for date in date range
# Using loop
from datetime import datetime

# initializing list
test_list = [datetime(2019, 12, 30), datetime(2018, 4, 4),
			datetime(2016, 12, 21), datetime(2021, 2, 2),
			datetime(2020, 2, 3), datetime(2017, 1, 1)]

# printing original list
print("The original list is : " + str(test_list))

# initializing date ranges
date_strt, date_end = datetime(2019, 3, 14), datetime(2020, 1, 4)

res = False
for ele in test_list:

	# checking for date in range
	if ele >= date_strt and ele <= date_end:
		res = True

# printing result
print("Does list contain any date in range : " + str(res))
