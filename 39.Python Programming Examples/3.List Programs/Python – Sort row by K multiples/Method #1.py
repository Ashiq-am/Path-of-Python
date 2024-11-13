# Python3 code to demonstrate working of
# Sort row by K multiples
# Using sort() + % operator + len()

# checking for multiples count


def k_mul(row):
	return len([ele for ele in row if ele % K == 0])


# initializing list
test_list = [[3, 4, 8, 1], [12, 32, 4, 16], [1, 2, 3, 4], [9, 7, 5]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# performing sort
test_list.sort(key=k_mul)

# printing result
print("Sorted result : " + str(test_list))
