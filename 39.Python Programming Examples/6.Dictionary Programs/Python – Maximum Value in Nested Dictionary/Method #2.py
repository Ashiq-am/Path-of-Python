# Python3 code to demonstrate working of
# Maximum Value in Nested Dictionary
# Using max() + dictionary comprehension

# initializing dictionary
test_dict = {'gfg': {'a': 15, 'b': 14},
             'is': {'d': 2, 'e': 10, 'f': 3},
             'best': {'g': 19}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Maximum Value in Nested Dictionary
# Using max() + dictionary comprehension
res = {key: max(val.values()) for key, val in test_dict.items()}

# printing result
print("The modified dictionary : " + str(res))
