# Python3 code to demonstrate working of
# Flatten and remove keys from Dictonary
# Using loop + recursion + isinstance()

# function to compute removal and flattening
def hlper_fnc(test_dict, rem_keys):
    if not isinstance(test_dict, dict):
        return test_dict
    res = {}

    for key, val in test_dict.items():
        rem = hlper_fnc(val, rem_keys)

        # performing removal
        if key not in rem_keys:
            res[key] = rem
        else:
            if isinstance(rem, dict):
                res.update(rem)
    return res


# initializing dictionary
test_dict = {'a': 14, 'b': 16, 'c': {'d': {'e': 7}}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing removal keys
rem_keys = ["c", "d"]

# calling helper function for task
res = hlper_fnc(test_dict, rem_keys)

# printing result
print("The removed and flattened dictionary : " + str(res))
