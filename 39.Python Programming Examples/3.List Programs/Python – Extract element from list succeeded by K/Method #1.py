# Python3 code to demonstrate working of
# Extract elements succeeded by K
# Using loop

# initializing list
test_list = [2, 3, 5, 7, 8, 5, 3, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# Using loop to extract elements succeeded by K
res = []
for idx in range(len(test_list) - 1):

	# checking for succession
	if test_list[idx + 1] == K:
		res.append(test_list[idx])

# printing result
print("Extracted elements list : " + str(res))
