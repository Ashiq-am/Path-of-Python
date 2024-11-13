# Python3 code to demonstrate working of
# Sort row by K multiples
# Using sorted() + lambda + len()

# initializing list
test_list = [[3, 4, 8, 1], [12, 32, 4, 16], [1, 2, 3, 4], [9, 7, 5]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# performing sort using sorted()
# lambda avoiding external function call
res = sorted(test_list, key=lambda row: len(
	[ele for ele in row if ele % K == 0]))

# printing result
print("Sorted result : " + str(res))
