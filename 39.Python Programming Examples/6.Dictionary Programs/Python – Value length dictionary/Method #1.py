# Python3 code to demonstrate working of
# Value length dictionary
# Using loop + len()

# initializing dictionary
test_dict = {1: 'gfg', 2: 'is', 3: 'best'}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Value length dictionary
# Using loop + len()
res = {}
for val in test_dict.values():
    res[val] = len(val)

# printing result
print("The value-size mapped dictionary is : " + str(res))
