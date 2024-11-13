# Python3 code to demonstrate working of
# Non K distant elements
# Using loop

# initializing list
test_list = [8, 10, 16, 20, 3, 1, 7]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

res = []
for ele in test_list:

	# check for K distant
	if ele + K not in test_list and ele - K not in test_list:
		res.append(ele)

# printing result
print("The filtered List : " + str(res))
