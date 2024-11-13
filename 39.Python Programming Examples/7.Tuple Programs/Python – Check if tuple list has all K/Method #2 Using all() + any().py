# Python3 code to demonstrate working of
# Check if tuple list has all K
# Using all() + any()

# initializing list
test_list = [(4, 4), (4, 4, 4), (4, 4), (4, 4, 4, 4), (4, )]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# Check if tuple list has all K
# Using all() + any()
res = any(all(val == K for val in tup) for tup in test_list)

# printing result
print("Are all elements K ? : " + str(res))
