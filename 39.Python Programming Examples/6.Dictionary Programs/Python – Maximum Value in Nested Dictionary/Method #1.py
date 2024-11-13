# Python3 code to demonstrate working of
# Maximum Value in Nested Dictionary
# Using loop

# initializing dictionary
test_dict = {'gfg': {'a': 15, 'b': 14},
             'is': {'d': 2, 'e': 10, 'f': 3},
             'best': {'g': 19}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Maximum Value in Nested Dictionary
# Using loop
res = {}
for key, val in test_dict.items():
    max_val = 0
    for ele in val.values():
        if ele > max_val:
            max_val = ele
    res[key] = max_val

# printing result
print("The modified dictionary : " + str(res))
