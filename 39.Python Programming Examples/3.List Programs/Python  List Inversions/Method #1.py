# Python3 code to demonstrate working of
# List Inversions
# Using map() + lambda + "~" operator

# initializing list
test_list = [7, 8, 9, 1, 10, 7]

# printing original list
print("The original list is : " + str(test_list))

# List Inversions
# Using map() + lambda + "~" operator
res = list(map(lambda x: ~x, test_list))

# printing result
print("The Bitwise Inversions of list elements are : " + str(res))
