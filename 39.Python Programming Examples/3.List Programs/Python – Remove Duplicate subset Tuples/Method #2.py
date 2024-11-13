# Python3 code to demonstrate working of
# Remove Duplicate subset Tuples
# Using all() + any()+ loop

# initializing lists
test_list = [(6, 9, 17, 18), (15, 34, 56), (6, 7), (6, 9), (15, 34)]

# printing original list
print("The original list is : " + str(test_list))

# Remove Duplicate subset Tuples
# Using all() + any() + loop
res = []
test_list = sorted(test_list, key = lambda x: len(x))
for idx, sub in enumerate(test_list):
	if any(all(ele in sub2 for ele in sub) for sub2 in test_list[idx + 1:]):
		pass
	else:
		res.append(sub)

# printing result
print("Tuple list after removal : " + str(res))
