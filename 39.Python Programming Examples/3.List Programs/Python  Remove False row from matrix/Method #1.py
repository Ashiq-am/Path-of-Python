# Python3 code to demonstrate
# removing False rows in matrix
# using list comprehension + count() + len()

# initializing matrix
test_list = [[1, True, 2], [False, False, 3],
			[False, False, False], [1, 0, 1]]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + count() + len()
# removing False rows in matrix
res = [sub for sub in test_list
	if sub.count(False) != len(sub)]

# print result
print("The list after removal of False rows : " + str(res))
