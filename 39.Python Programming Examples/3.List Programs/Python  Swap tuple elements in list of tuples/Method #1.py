# Python3 code to demonstrate working of
# Swap tuple elements in list of tuples
# Using list comprehension

# initializing list
test_list = [(3, 4), (6, 5), (7, 8)]

# printing original list
print("The original list is : " + str(test_list))

# Swap tuple elements in list of tuples
# Using list comprehension
res = [(sub[1], sub[0]) for sub in test_list]

# printing result
print("The swapped tuple list is : " + str(res))
