# Python3 code to demonstrate working of
# Test if dates are consecutive
# Using days() + loop
from datetime import datetime, timedelta

# initializing list
test_list = [datetime(2019, 12, 30), datetime(2019, 12, 31),
			datetime(2020, 1, 1), datetime(2020, 1, 2),
			datetime(2020, 1, 3), datetime(2020, 1, 4)]

# printing original list
print("The original list is : " + str(test_list))

# using loop for iterating all elements
res = True
for idx in range(1, len(test_list)):

	# checking for 1 day time difference
	if (test_list[idx] - test_list[idx - 1]).days != 1:
		res = False
		break

# printing result
print("Are dates consecutive : " + str(res))
