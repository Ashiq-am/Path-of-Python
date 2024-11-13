# Python3 code to demonstrate working of
# Range Numbers not in set
# Using "-" operator

# initializing set
test_set = {6, 4, 2, 7, 9}

# printing original set
print("The original set is : " + str(test_set))

# initializing range
low, high = 5, 10

# using "-" operator to get difference
res = list(set(range(low, high)) - test_set)

# printing result
print("Elements not in set : " + str(res))
