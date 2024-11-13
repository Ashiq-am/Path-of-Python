# Python3 code to demonstrate working of
# Test for Non-neighbours in List
# Using loop

# initializing list
test_list = [3, 7, 2, 1, 4, 5, 7, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing i, j
i, j = 7, 4

res = True
for idx in range(1, len(test_list) - 1):
	if test_list[idx] == i:

		# check for surrounding element to be j if i
		if test_list[idx - 1] == j or test_list[idx + 1] == j:
			res = False
			break

# printing result
print("Are i, j Non-neighbours' : " + str(res))
