# Python3 code to demonstrate
# Dual element Rows Combinations
# using list comprehension + enumerate()
from collections import defaultdict

# Initializing list
test_list = [[3, 4], [5, 6], [7, 8]]

# printing original list
print("The original list is : " + str(test_list))

# Dual element Rows Combinations
# using list comprehension + enumerate()
res = [test_list[idx - len(test_list)] + test_list[idx + 1 - len(test_list)]
	for idx, ele in enumerate(test_list)]

# printing result
print ("Combination of dual rows list is : " + str(res))
