# Python3 code to demonstrate working of
# Row lengths counts
# Using Counter() + map() + len()
from collections import Counter

# initializing list
test_list = [[6, 3, 1], [8, 9], [2],
			[10, 12, 7], [4, 11]]

# printing original list
print("The original list is : " + str(test_list))

# Counter gets the frequencies of counts
# map and len gets lengths of sublist
res = dict(Counter(map(len, test_list)))

# printing result
print("Row length frequencies : " + str(res))
