# Python3 code to demonstrate working of
# Reorder for consecutive elements
# Using Counter() + loop + items()
from collections import Counter

# initializing list
test_list = [4, 7, 5, 4, 1, 4, 1, 6, 7, 5]

# printing original lists
print("The original list is : " + str(test_list))

# getting frequency
freqs = Counter(test_list)
res = []

# reordering basis of frequency
for val, cnt in freqs.items():
	res.extend([val]*cnt)

# printing result
print("Reordered List : " + str(res))
