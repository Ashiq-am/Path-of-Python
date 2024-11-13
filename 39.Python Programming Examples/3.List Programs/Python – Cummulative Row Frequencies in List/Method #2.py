# Python3 code to demonstrate working of
# Cummulative Row Frequencies
# Using sum() + list comprehension

# initializing list
test_list = [[10, 2, 3, 2, 3],
			[5, 5, 4, 7, 7, 4],
			[1, 2], [1, 1, 2, 2, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing ele_list
ele_list = [1, 2, 7]

# getting summation
res = [sum(ele in ele_list for ele in sub) for sub in test_list]

# printing result
print("Cummulative Frequencies : " + str(res))
