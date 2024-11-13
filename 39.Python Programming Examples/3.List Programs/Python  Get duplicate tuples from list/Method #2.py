# Python3 code to demonstrate working of
# Get duplicate tuples from list
# Using list comprehension + Counter() + items()
from collections import Counter

# initialize list
test_list = [(3, 4), (4, 5), (3, 4),
			(3, 4), (4, 5), (6, 7)]

# printing original list
print("The original list : " + str(test_list))

# Get duplicate tuples from list
# Using list comprehension + Counter() + items()
res = [ele for ele, count in Counter(test_list).items()
										if count > 1]

# printing result
print("All the duplicates from list are : " + str(res))
