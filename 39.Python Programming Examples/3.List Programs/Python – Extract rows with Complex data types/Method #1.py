# Python3 code to demonstrate working of
# Extract rows with Complex data types
# Using list comprehension + isinstance() + any()

# initializing list
test_list = [[4, 2, 5], [1, [3, 4], 9], [5], [7, (2, 3), 3, 9]]

# printing original list
print("The original list is : " + str(test_list))

# checking for any of list, set, tuple or
# dictionary as complex structures
res = [row for row in test_list if any(isinstance(ele, list) or isinstance(ele, tuple)
									or isinstance(ele, dict) or isinstance(ele, set) for ele in row)]

# printing result
print("Filtered Rows : " + str(res))
