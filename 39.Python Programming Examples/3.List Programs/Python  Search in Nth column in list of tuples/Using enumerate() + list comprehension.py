# Python3 code to demonstrate working of
# Search in Nth column in list of tuples
# Using enumerate() + list comprehension

# initializing list
test_list = [('gfg', 1, 9), ('is', 5, 10), (8, 'best', 13)]

# printing list
print("The original list : " + str(test_list))

# initializing Nth column
N = 2

# initializing num
ele = 10

# Search in Nth column in list of tuples
# Using enumerate() + list comprehension
res = [idx for idx, val in enumerate(test_list) if val[N] == ele]

# Printing result
print("Row of desired element is : " + str(res))
