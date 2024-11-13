# Python3 code to demonstrate working of
# Check if one dictionary is subset of other
# Using all() + items()

# Initialize dictionaries
test_dict1 = {'gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}
test_dict2 = {'gfg': 1, 'is': 2, 'best': 3}

# printing original dictionaries
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))

# Using all() + items()
# Check if one dictionary is subset of other
res = all(test_dict1.get(key, None) == val for key, val
          in test_dict2.items())

# printing result
print("Does dict2 lie in dict1 ? : " + str(res))
