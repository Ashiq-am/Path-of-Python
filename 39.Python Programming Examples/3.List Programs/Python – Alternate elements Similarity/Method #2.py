# Python3 code to demonstrate working of
# Alternate elements Similarity
# Using all() + generator expression

# initializing lists
test_list = [5, 3, 5, 2, 5, 8, 5]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 5

# all() to encapsulate whole logic into one expression
res = all(test_list[idx] == K for idx in range(0, len(test_list), 2))

# printing result
print("Are all alternate elements equal to K : " + str(res))
