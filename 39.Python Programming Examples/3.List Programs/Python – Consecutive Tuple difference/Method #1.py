# Python3 code to demonstrate working of
# Consecutive Tuple difference
# Using list comprehension

# initializing lists
test_list = [(6, 3), (1, 4), (8, 5), (3, 5)]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension to perform absolute difference
# using abs() for difference
res = [(abs(test_list[idx + 1][0] - test_list[idx][0]), abs(test_list[idx + 1][1] - test_list[idx][1]))
	for idx in range(len(test_list) - 1)]

# printing result
print("The extracted list : " + str(res))
