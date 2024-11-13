# Python3 code to demonstrate working of
# Nearest K Sort
# Using sort() + abs()

# getting absolute difference
def get_diff(ele):

	# returning absolute difference
	return abs(ele - K)


# initializing list
test_list = [6, 7, 4, 11, 17, 8, 3]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 10

# performing inplace sort using sort()
test_list.sort(key=get_diff)

# printing result
print("Sorted List : " + str(test_list))
