# Python3 code to demonstrate working of
# Test for all Even elements in List Range
# Using all() + list comprehension

# initializing list
test_list = [3, 1, 4, 6, 8, 10, 1, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 2, 5

# all() checks for all even elements
res = all(test_list[idx] % 2 == 0 for idx in range(i, j + 1))

# printing result
print("Are all elements even in range : " + str(res))
