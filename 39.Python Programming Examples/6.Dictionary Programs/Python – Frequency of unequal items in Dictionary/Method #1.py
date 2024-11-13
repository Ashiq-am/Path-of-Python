# Python3 code to demonstrate working of
# Dissimilar items frequency in Dictionary
# Using dictionary comprehension

# initializing dictionaries
test_dict1 = {'gfg' : 1, 'is' : 2, 'best' : 3}
test_dict2 = {'gfg' : 1, 'is' : 2, 'good' : 3}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# Dissimilar items frequency in Dictionary
# Using dictionary comprehension
res = {key: test_dict1[key] for key in test_dict1 if key not in test_dict2}

# printing result
print("The number of uncommon items are : " + str(len(res)))
