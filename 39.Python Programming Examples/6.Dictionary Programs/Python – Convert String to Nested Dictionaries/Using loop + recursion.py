# Python3 code to demonstrate working of
# Convert String to Nested Dictionaries
# Using loop

def helper_fnc(test_str, sep):


    if sep not in test_str:
        return test_str
    key, val = test_str.split(sep, 1)
    return {key: helper_fnc(val, sep)}

# initializing string
test_str = 'gfg_is_best_for_geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing separator
sep = '_'

# Convert String to Nested Dictionaries
# Using loop
res = helper_fnc(test_str, sep)

# printing result
print("The nested dictionary is : " + str(res))
