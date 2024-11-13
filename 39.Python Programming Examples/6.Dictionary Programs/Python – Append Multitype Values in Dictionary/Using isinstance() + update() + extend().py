# Python3 code to demonstrate working of
# Append Multitype Values in Dictionary
# Using isinstance() + update() + extend()

# helper_fnc
def update_dictionary(key, val, test_dict):
    if key not in test_dict:
        current_dict[key] = value

    elif type(val) not in [str, list, dict]:
        raise ValueError("Invalid Data Type")

    elif isinstance(val, list):
        test_dict[key].extend(val)

    elif isinstance(val, dict):
        test_dict[key].update(val)

    else:
        test_dict[key] = test_dict[key] + val

    return test_dict


# initializing dictionary
test_dict = {'gfg': "geekfor", 'is': {'a': 5, 'b': 6}, 'best': [1, 2, 3]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing dict, string and append
up_dict = {'c': 7}
up_str = 'geeks'
up_list = [4, 5]

# Append Multitype Values in Dictionary
# Using isinstance() + update() + extend()
res = update_dictionary('gfg', up_str, test_dict)
res = update_dictionary('is', up_dict, res)
res = update_dictionary('best', up_list, res)

# printing result
print("The update dictionary : " + str(res))
