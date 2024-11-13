# Python3 code to demonstrate
# Count Similar pair in dual list
# using sum() + list comprehension + groupby() + sorted()
from itertools import groupby

# initializing list
test_list = [[1, 2], [2, 1], [3, 4], [4, 3], [5, 4]]

# printing original list
print ("The original list is : " + str(test_list))

# Count Similar pair in dual list
# using sum() + list comprehension + groupby() + sorted()
res = [(*temp, sum(1 for idx in elements))
	for temp, elements in groupby(test_list, key = lambda j : sorted(j))]

# printing result
print ("The dual list similarity counts : " + str(res))
