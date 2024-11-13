# Python3 code to demonstrate working of
# Reverse Kth rows in Matrix
# Using Slicing + list comprehension

# initializing list
test_list = [[5, 3, 2], [8, 6, 3], [3, 5, 2],
			[3, 6], [3, 7, 4], [2, 9]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# using enumerate() to get index and elements.
# list comprehension to perform of iteration
res = [ele[::-1] if (idx + 1) % K == 0 else ele for idx,
	ele in enumerate(test_list)]

# printing result
print("After reversing every Kth row: " + str(res))
