# Python3 code to demonstrate working of
# Extract tuple supersets from List
# Using all() + list comprehension + Counter
from collections import Counter

# initializing list
test_list = [(5, 6, 8), (4, 2, 7), (9, 6, 5, 6)]

# printing original list
print("The original list is : " + str(test_list))

# initializing tuple
test_tup = (6, 6, 5)

# Extract tuple supersets from List
# Using all() + list comprehension + Counter
res = [sub for sub in test_list if
	all(Counter(sub)[x] >= Counter(test_tup)[x]
	for x in Counter(test_tup))]

# printing result
print("The superset tuples : " + str(res))
