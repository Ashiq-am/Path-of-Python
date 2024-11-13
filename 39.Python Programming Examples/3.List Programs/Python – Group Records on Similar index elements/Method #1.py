# Python3 code to demonstrate working of
# Group Records on Similar index elements
# Using defaultdict() + loop
from collections import defaultdict

# initializing list
test_list = [(4, 7, 13), (4, 5, 7), (6, 7, 10), (4, 5, 15), (6, 7, 12)]

# printing original list
print("The original list is : " + str(test_list))

# Group Records on Similar index elements
# Using defaultdict() + loop
temp = defaultdict(list)
for a, b, c in test_list:
	temp[a, b].append(c)
res = tuple((*key, val) for key, val in temp.items())

# printing result
print("Tuples after grouping : " + str(res))
