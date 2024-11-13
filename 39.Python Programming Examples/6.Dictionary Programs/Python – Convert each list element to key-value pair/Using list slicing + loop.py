# Python3 code to demonstrate working of
# Convert each list element to key-value pair
# Using loop + list slicing

# initializing list
test_list = [2323, 82, 129388, 234, 95]

# printing original list
print("The original list is : " + str(test_list))

res = dict()
for ele in test_list:

	# constructing key and values
	mid_idx = len(str(ele)) // 2
	key = int(str(ele)[:mid_idx])
	val = int(str(ele)[mid_idx:])

	# item assignment
	res[key] = val

# printing result
print("Constructed Dictionary : " + str(res))
