# Python3 code to demonstrate working of
# Update dictonary with dictionary list
# Using update() + loop

# initializing dictionary
test_dict = {"Gfg": 2, "is": 1, "Best": 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing dictionary list
dict_list = [{'for': 3, 'all': 7}, {'geeks': 10}, {'and': 1, 'CS': 9}]

for dicts in dict_list:
    # updating using update()
    test_dict.update(dicts)

# printing result
print("The updated dictionary : " + str(test_dict))
