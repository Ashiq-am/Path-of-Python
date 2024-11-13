# Python3 code to demonstrate
# Row lengths in matrix
# using max() + map() + sum() + list comprehension

# initializing list
test_list = [[4, 5, 6], [7, 8], [2]]

# printing original list
print("The original list : " + str(test_list))

# using max() + map() + sum() + list comprehension
# Row lengths in matrix
res = [sum(len(row) > idx for row in test_list)
	for idx in range(max(map(len, test_list)))]

# print result
print("The row lengths in matrix : " + str(res))
