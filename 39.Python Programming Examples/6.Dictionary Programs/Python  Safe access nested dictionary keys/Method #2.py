# Python code to demonstrate working of
# Safe access nested dictionary key
# Using reduce() + lambda

# initializing dictionary
test_dict = {'Gfg' : {'is' : 'best'}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using reduce() + lambda
# Safe access nested dictionary key
keys = ['Gfg', 'is']
res = reduce(lambda val, key: val.get(key) if val else None, keys, test_dict)

# printing result
print("The nested safely accessed value is : " + str(res))
