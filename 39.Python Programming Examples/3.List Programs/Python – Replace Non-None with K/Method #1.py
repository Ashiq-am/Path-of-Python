# Python3 code to demonstrate working of
# Replace Non-None with K
# Using list comprehension

# initializing list
test_list = [59, 236, None, 3, '']

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 'Gfg'

# Replace Non-None with K
# Using list comprehension
res = [K if ele else ele for ele in test_list]

# printing result
print("List after replacement : " + str(res))
