# Python3 code to demonstrate working of
# Test K in Range
# Using all()

# initializing list
test_list = [2, 3, 4, 4, 4, 4, 6, 7, 8, 2]

# printing original list
print("The original list is : " + str(test_list))

# initializing Range
i, j = 2, 5

# initializing K
K = 4

# all() to check all elements to be K
res = all(test_list[idx] == K for idx in range(i, j + 1))

# printing result
print("Are all elements in range K ? : " + str(res))
