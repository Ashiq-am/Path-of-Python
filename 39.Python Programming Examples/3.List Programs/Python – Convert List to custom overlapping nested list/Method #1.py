# Python3 code to demonstrate working of
# Convert List to custom overlapping Matrix
# Using list slicing + loop

# initializing list
test_list = [3, 5, 6, 7, 3, 9, 1, 10]

# printing original list
print("The original list is : " + str(test_list))

# initializing step, size
step, size = 2, 4

res = []
for idx in range(0, len(test_list), step):

	# slicing list
	res.append(test_list[idx: idx + size])

# printing result
print("The created Matrix : " + str(res))
