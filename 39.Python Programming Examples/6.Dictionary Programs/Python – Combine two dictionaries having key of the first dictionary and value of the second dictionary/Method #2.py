# Python3 code to demonstrate working of
# Assign similar index values in Dictionary
# Using zip() + values()

# initializing dictionaries
test_dict1 = {"Gfg": 20, "is": 36, "best": 100}
test_dict2 = {"Gfg2": 26, "is2": 19, "best2": 70}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# using zip() to perform required dict. mapping
res = dict(zip(test_dict1, test_dict2.values()))

# printing result
print("Mapped dictionary : " + str(res))
