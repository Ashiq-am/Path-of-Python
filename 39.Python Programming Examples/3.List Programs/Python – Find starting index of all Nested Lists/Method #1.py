# Python3 code to demonstrate working of
# Initial element index in Matrix
# Using loop

# initializing list
test_list = [[5], [9, 3, 1, 4], [3, 2], [4, 7, 8, 3, 1, 2], [3, 4, 5]]

# printing original list
print("The original list is : " + str(test_list))

res = []
lens = 0
for sub in test_list:

	# lengths of sublist computed
	res.append(lens)
	lens += len(sub)

# printing result
print("Initial element indices : " + str(res))
