# Python3 code to demonstrate
# Dual Element row with Maximum difference
# using max() + lambda + list comprehension

# Initializing list
test_list = [[5, 10], [1, 3], [4, 11], [1, 2]]

# printing original list
print("The original list is : " + str(test_list))

# Dual Element row with Maximum difference
# using max() + lambda + list comprehension
res = max(test_list, key = lambda ele: abs(ele[0] - ele[1]))

# printing result
print ("The maximum difference row is : " + str(res))
