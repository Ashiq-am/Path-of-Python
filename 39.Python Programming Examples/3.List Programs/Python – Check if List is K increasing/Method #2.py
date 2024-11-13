# Python3 code to demonstrate working of
# Check if List is K increasing
# Using all() + generator expression

# initializing list
test_list = [4, 7, 10, 13, 16, 19]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# using all() to check for all elements
res = all(test_list[idx + 1] == test_list[idx] + K for idx in range(len(test_list) - 1))

# printing results
print("Is list K increasing ? : " + str(res))
