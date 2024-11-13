# Python3 code to demonstrate working of
# Sort Matrix by K Sized Subarray Maximum Sum
# Using sorted() + lambda + max() + sum() + slicing

# initializing list
test_list = [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1],
			[4, 3, 9, 3, 9], [5, 4, 3, 2, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# sorted() performs inplace sort
# lambda function injects comparison logic
res = sorted(test_list, key=lambda row: max(
	sum(row[idx: idx + K]) for idx in range(len(row) - K)))

# printing result
print("The sorted result : " + str(res))
