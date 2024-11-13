# Python3 code to demonstrate working of
# Resolve Transitivity in Dictionary
# Using reverse dictionary + loop

# initializing dictionary
test_dict = {'a': 3, 'b': 4, 3: 5, 'l': 7, 4: 'd', 7: 'k'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Resolve Transitivity in Dictionary
# Using reverse dictionary + loop
temp = {val: key for key, val in test_dict.items()}
for val in temp:
    if val in test_dict:
        test_dict.pop(temp[val])
    test_dict[temp[val]] = test_dict[val]
    test_dict.pop(val)

# printing result
print("The resolved dictionary : " + str(test_dict))
