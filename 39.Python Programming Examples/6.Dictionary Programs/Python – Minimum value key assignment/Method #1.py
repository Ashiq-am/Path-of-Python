# Python3 code to demonstrate working of
# Minimum value key assignment
# Using dictionary comprehension + min() + items()

# initializing dictionaries
test_dict1 = {"gfg": 1, "is": 7, "best": 8}
test_dict2 = {"gfg": 2, "is": 2, "best": 10}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# using min() to assign min values
res = {key: min(val, test_dict2[key]) for key, val in test_dict1.items()}

# printing result
print("The minimum value keys : " + str(res))
