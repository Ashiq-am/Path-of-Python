# Python3 code to demonstrate working of
# Remove unwanted Keys associations
# Using isinstance() + loop + recursion

def helper_fnc(test_dict, unw_keys):
    temp = {}
    for key, val in test_dict.items():
        if key in unw_keys:
            continue
        if isinstance(val, dict):
            temp[key] = helper_fnc(val, unw_keys)
        else:
            temp[key] = val
    return temp


# initializing dictionary
test_dict = {"Gfg": {'is': 45, 'good': 15},
             'best': {'for': {'geeks': {'CS': 12}}}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing unwanted keys
unw_keys = ['is', 'geeks']

# Remove unwanted Keys associations
# Using isinstance() + loop + recursion
res = helper_fnc(test_dict, unw_keys)

# printing result
print("The filtered dictionary : " + str(res))
