# Python3 code to demonstrate working of
# Extract rows with Complex data types
# Using filter() + lambda + isinstance()

# initializing list
test_list = [[4, 2, 5], [1, [3, 4], 9], [5], [7, (2, 3), 3, 9]]

# printing original list
print("The original list is : " + str(test_list))

# checking for any of list, set, tuple or dictionary as complex structures
res = list(filter(lambda row: any(isinstance(ele, list) or isinstance(ele, tuple)
								or isinstance(ele, dict) or isinstance(ele, set) for ele in row), test_list))

# printing result
print("Filtered Rows : " + str(res))
