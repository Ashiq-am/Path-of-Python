# Python3 code to demonstrate working of
# Replace None with Empty Dictionary
# Using recursion + isinstance()

# helper function to perform task


def replace_none(test_dict):
    # checking for dictionary and replacing if None
    if isinstance(test_dict, dict):

        for key in test_dict:
            if test_dict[key] is None:
                test_dict[key] = {}
            else:
                replace_none(test_dict[key])

    # checking for list, and testing for each value
    elif isinstance(test_dict, list):
        for val in test_dict:
            replace_none(val)


# initializing dictionary
test_dict = {"Gfg": {1: None, 7: 4}, "is": None,
             "Best": [1, {5: None}, 9, 3]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# calling helper fnc
replace_none(test_dict)

# printing result
print("The converted dictionary : " + str(test_dict))
