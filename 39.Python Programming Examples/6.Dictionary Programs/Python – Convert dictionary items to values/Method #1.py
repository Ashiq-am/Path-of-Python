# Python3 code to demonstrate working of
# Convert dictionary items to values
# Using loop

# initializing dictionary
test_dict = {'Gfg': 1, 'is': 2, 'best': 3}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Convert dictionary items to values
# Using loop
res = []
for key, val in test_dict.items():
    res.append({"key": key, "value": val})

# printing result
print("Converted Dictionary : " + str(res))
