# Python3 code to demonstrate working of
# Combine list with other list elements
# Using zip() + len() + list()

# initializing list
test_list = [3, 5, 7, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing pair list
pair_list = ['Gfg', 'is', 'best']

# using zip() to pair element with pair list size
res = list(zip([test_list] * len(pair_list), pair_list))

# printing result
print("The paired list : " + str(res))
