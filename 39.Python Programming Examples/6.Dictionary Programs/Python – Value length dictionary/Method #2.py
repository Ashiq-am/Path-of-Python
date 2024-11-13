# Python3 code to demonstrate working of
# Value length dictionary
# Using dictionary comprehension

# initializing dictionary
test_dict = {1: 'gfg', 2: 'is', 3: 'best'}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Value length dictionary
# Using dictionary comprehension
res = {val: len(val) for val in test_dict.values()}

# printing result
print("The value-size mapped dictionary is : " + str(res))
