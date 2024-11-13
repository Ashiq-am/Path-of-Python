# Python3 code to demonstrate working of
# Inter Matrix Grouping
# Using defaultdict() + loop
from collections import defaultdict

# initializing lists
test_list1 = [[5, 8], [2, 0], [8, 4], [9, 3]]
test_list2 = [[8, 1], [9, 7], [2, 10], [5, 6]]

# printing original list
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# initializing mapping list
res = defaultdict(list)

# concatenation matrix using 2 lists
for key, val in test_list1 + test_list2:
	res[key].append(val)

# printing result
print("The Grouped Matrix : " + str(dict(res)))
