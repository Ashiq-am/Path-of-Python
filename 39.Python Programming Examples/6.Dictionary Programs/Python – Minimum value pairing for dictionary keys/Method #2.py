# Python3 code to demonstrate working of
# Minimum value pairing for dictionary keys
# Using groupby() + itemgetter() + zip()
from operator import itemgetter
from itertools import groupby

# initializing lists
test_list1 = [4, 7, 4, 8, 7, 9]
test_list2 = [5, 7, 2, 9, 3, 4]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using zip() to bind key and value lists
# groupby() to group similar value.
# 0th, first element is extracted to be smallest
# using itemgetter()
temp = sorted(zip(test_list1, test_list2))
res = {key: min(val for _, val in group)
	for key, group in groupby(sorted(temp), itemgetter(0))}

# printing result
print("The minimum paired dictionary : " + str(res))
