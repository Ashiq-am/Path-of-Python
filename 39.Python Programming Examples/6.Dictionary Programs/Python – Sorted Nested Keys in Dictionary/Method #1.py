# Python3 code to demonstrate working of
# Sorted Nested Keys in Dictionary
# Using yield + isinstance() + loop

def hlper_fnc(test_dict):
    for key, val in test_dict.items():
        yield key
        if isinstance(val, dict):
            yield from val


# initializing dictionary
test_dict = {'gfg': 43, 'is': {'best': 14, 'for': 35, 'geeks': 42}, 'and': {'CS': 29}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Sorted Nested Keys in Dictionary
# Using yield + isinstance() + loop
res = sorted(hlper_fnc(test_dict))

# printing result
print("The sorted nested keys : " + str(res))
