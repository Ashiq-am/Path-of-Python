# Python3 code to demonstrate working of
# Alternate Default Key Value
# Using get()

# initializing dictionary
test_dict = {'gfg': {'a': 1, 'b': 2, 'c': 3}, 'best': {'a': 3, 'c': 4}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# alternate key
alt_key = 'gfg'

# Alternate Default Key Value
# Using get()
res = test_dict.get('best').get('b', test_dict.get(alt_key)['b'])

# printing result
print("The required value : " + str(res))
