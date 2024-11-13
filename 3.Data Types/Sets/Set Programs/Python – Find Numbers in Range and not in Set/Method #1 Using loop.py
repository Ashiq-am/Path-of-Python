# Python3 code to demonstrate working of
# Range Numbers not in set
# Using loop

# initializing set
test_set = {6, 4, 2, 7, 9}

# printing original set
print("The original set is : " + str(test_set))

# initializing range
low, high = 5, 10

res = []
for ele in range(low, high):

	# getting elements not in set
	if ele not in test_set:
		res.append(ele)

# printing result
print("Elements not in set : " + str(res))
