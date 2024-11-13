# initializing list
test_list = [5, 6, 3, 2, 7, 1, 9, 10, 8]

# printing original list
print("The original list is : " + str(test_list))

# initializing skips
K = 3

res = []
for idx in range(0, K):

	# 3rd arg. of slicing skips by K
	res.append(test_list[idx::K])

# printing result
print("Stepped splitted List : " + str(res))
