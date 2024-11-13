# Python3 code to demonstrate working of
# Group first elements by second elements in Tuple list
# Using loop + groupby() + sorted() + list comprehension + lambda
from itertools import groupby

# initializing list
test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]

# printing original list
print("The original list is : " + str(test_list))

res = dict()

# forming equal groups
for key, val in groupby(sorted(test_list, key = lambda ele: ele[1]), key = lambda ele: ele[1]):
	res[key] = [ele[0] for ele in val]

# printing results
print("Grouped Dictionary : " + str(res))
