# Python3 code to demonstrate working of
# Remove Tuples with difference greater than K
# Using filter() + lambda + abs()

# initializing list
test_list = [(4, 8), (1, 7), (9, 12), (3, 12), (2, 10)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# Using filter() and lambda function for filtering
res = list(filter(lambda sub: abs(sub[0] - sub[1]) <= K, test_list))

# printing result
print("Tuples List after removal : " + str(res))
