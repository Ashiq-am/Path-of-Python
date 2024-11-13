# Python3 code to demonstrate working of
# Multiple Indices from list elements
# Using setdefault() + loop

# initializing list
test_list = [4, 5, 3, 7, 8, 3, 2, 4, 3, 5, 8, 3]

# printing original list
print("The original list is : " + str(test_list))

# initializing get_list
get_list = [7, 5, 3]

# getting all elements indices
ele_indices = dict()
for idx, val in enumerate(test_list):
	ele_indices.setdefault(val, []).append(idx)

# filtering only required elements
res = [ele_indices.get(idx, [None]) for idx in get_list]

# printing result
print("Filtered Indices of elements in list 1 : " + str(res))
