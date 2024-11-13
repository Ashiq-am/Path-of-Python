# Python3 code to demonstrate working of
# Index Directory of Elements

# Using dictionary comprehension + groupby() +
# enumerate() + sorted() + itemgetter()
from itertools import groupby
from operator import itemgetter

# initializing list
test_list = [7, 6, 3, 7, 8, 3, 6, 7, 8]

# printing original list
print("The original list is : " + str(test_list))

# after grouping after sorting
# and rearranging and assigning values with index
res = {key: [idx for idx, _ in groups] for key, groups in groupby(
	sorted(enumerate(test_list), key=itemgetter(1)), key=itemgetter(1))}

# printing result
print("Index Directory : " + str(res))
