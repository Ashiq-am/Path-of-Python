# Python3 code to demonstrate working of
# Maximum length consecutive positive elements
# Using groupby() + defaultDict() + max()
from collections import defaultdict
from itertools import groupby

# initializing list
test_list = [4, 5, -4, -1, -7, 2, 5, 6, -2, -9, -10]

# printing original list
print("The original list : " + str(test_list))

# Maximum length consecutive positive elements
# Using groupby() + defaultDict() + max()
counter = defaultdict(list)
for key, val in groupby(test_list, lambda ele: "plus" if ele >= 0 else "minus"):
	counter[key].append(len(list(val)))
res = []
for key in ('plus', 'minus'):
	res.append(counter[key])

# printing result
print("Maximum elements run length : " + str(max(res[0])))
print("Maximum negative elements run length : " + str(max(res[1])))
