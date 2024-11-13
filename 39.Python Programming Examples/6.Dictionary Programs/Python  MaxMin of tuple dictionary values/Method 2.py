# Python3 code to demonstrate working of
# Max / Min of tuple dictionary values
# Using tuple() + map() + values() + * operator

# Initializing dictionary
test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3, 2), 'best' : (1, 4, 9)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Max / Min of tuple dictionary values
# Using tuple() + map() + values() + * operator
res = tuple(map(min, *test_dict.values()))

# printing result
print("The minimum values from each index is : " + str(res))
