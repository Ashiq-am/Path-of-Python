# Python3 code to demonstrate working of
# Replace Non-None with K
# Using map() + lambda()

# initializing list
test_list = [59, 236, None, 3, '']

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 'Gfg'

# Replace Non-None with K
# Using map() + lambda()
res = list(map(lambda ele: K if ele else ele, test_list))

# printing result
print("List after replacement : " + str(res))
