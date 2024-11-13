# Python3 code to demonstrate working of
# Test K in Range
# Using any()

# initializing list
test_list = [2, 3, 4, 4, 4, 4, 6, 7, 8, 2]

# printing original list
print("The original list is : " + str(test_list))

# initializing Range
i, j = 2, 5

# initializing K
K = 4

# any() to check if any element other than K present
# negation gives result
res = not any(test_list[idx] != K for idx in range(i, j + 1))

# printing result
print("Are all elements in range K ? : " + str(res))
