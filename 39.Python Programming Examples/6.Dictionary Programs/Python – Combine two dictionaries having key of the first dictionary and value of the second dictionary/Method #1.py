# Python3 code to demonstrate working of
# Assign similar index values in Dictionary
# Using loop + keys()

# initializing dictionaries
test_dict1 = {"Gfg": 20, "is": 36, "best": 100}
test_dict2 = {"Gfg2": 26, "is2": 19, "best2": 70}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# extracting keys and values
keys1 = list(test_dict1.keys())
vals2 = list(test_dict2.values())

# assigning new values
res = dict()
for idx in range(len(keys1)):
    res[keys1[idx]] = vals2[idx]

# printing result
print("Mapped dictionary : " + str(res))
