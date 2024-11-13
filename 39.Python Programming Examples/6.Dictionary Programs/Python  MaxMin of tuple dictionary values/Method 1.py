# Python3 code to demonstrate working of
# Max / Min of tuple dictionary values
# Using tuple() + min()/max() + zip() + values()

# Initializing dictionary
test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3, 2), 'best' : (1, 4, 9)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Max / Min of tuple dictionary values
# Using tuple() + min()/max() + zip() + values()
res = tuple(max(x) for x in zip(*test_dict.values()))

# printing result
print("The maximum values from each index is : " + str(res))
