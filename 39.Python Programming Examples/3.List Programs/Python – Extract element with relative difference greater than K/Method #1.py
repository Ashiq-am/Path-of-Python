# Python3 code to demonstrate working of
# Extract element with relative difference
# greater than K Using loop

# initializing list
test_list = [2, 7, 4, 1, 9, 2, 3, 10, 1, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

res = []
for idx in range(1, len(test_list)):

	# using abs to get absolute difference
	if abs(test_list[idx - 1] - test_list[idx]) > K and abs(test_list[idx + 1] - test_list[idx]) > K:
		res.append(test_list[idx])

# printing result
print("The extracted difference elements : " + str(res))
