# Python3 code to demonstrate working of
# Cross mapping of Two dictionary value lists
# Using loop + setdefault() + extend()

# initializing dictionaries
test_dict1 = {"Gfg": [4, 7], "Best": [8, 6], "is": [9, 3]}
test_dict2 = {6: [15, 9], 8: [6, 3], 7: [9, 8], 9: [10, 11]}

# printing original lists
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

res = {}

# getting all values of first dictionary
for key, val in test_dict1.items():
    for key1 in val:
        # getting result with default value list and extending
        # according to value optained from get()
        res.setdefault(key, []).extend(test_dict2.get(key1, []))

# printing result
print("The constructed dictionary : " + str(res))
