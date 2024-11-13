# Python3 code to demonstrate working of
# Columns to Dictionary Conversion in Matrix
# Using dictionary comprehension + list comprehension

# initializing list
test_list = [[4, 5, 7], [10, 8, 3], [19, 4, 6], [9, 3, 6]]

# printing original list
print("The original list : " + str(test_list))

# dictionary comprehension performing re making of result
# dictionary
res = {test_list[0][idx]: [test_list[ele][idx]
	for ele in range(1, len(test_list))]
	for idx in range(len(test_list[0]))}

# printing result
print("Reformed dictionary : " + str(res))
