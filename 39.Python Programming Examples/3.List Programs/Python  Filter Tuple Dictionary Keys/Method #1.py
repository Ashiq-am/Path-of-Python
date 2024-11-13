# Python3 code to demonstrate working of
# Filter Tuple Dictionary Keys
# Using list comprehension

# Initializing dict
test_dict = {(5, 6) : 'gfg', (1, 2, 8) : 'is', (9, 10) : 'best'}

# printing original dict
print("The original dict is : " + str(test_dict))

# Initializing K
K = 5

# Filter Tuple Dictionary Keys
# Using list comprehension
res = [ele for key in test_dict for ele in key if ele > K]

# printing result
print("The filtered dictionary tuple key elements are : " + str(res))
