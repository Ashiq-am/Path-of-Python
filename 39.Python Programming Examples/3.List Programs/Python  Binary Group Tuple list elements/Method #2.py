# Python3 code to demonstrate working of
# Binary Group Tuple list elements
# using defaultdict() + list comprehension + sorted() + items()
from collections import defaultdict

# initialize list
test_list = [(1, 56, 'M'), (1, 14, 'F'), (2, 43, 'F'), (2, 10, 'M')]

# printing original list
print("The original list : " + str(test_list))

# Binary Group Tuple list elements
# using defaultdict() + list comprehension + sorted() + items()
temp = defaultdict(list)
for ele in test_list:
	temp[ele[0]].append(ele[1])
res = sorted((key, ) + tuple(val) for key, val in temp.items())

# printing result
print("The list after binary grouping : " + str(res))
