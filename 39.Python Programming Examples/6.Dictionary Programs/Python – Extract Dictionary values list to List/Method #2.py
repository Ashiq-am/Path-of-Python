# Python3 code to demonstrate working of
# Extracting Dictionary values list to List
# Using map()

# initializing dictionary
test_dict = {'gfg': [4, 6, 7, 8],
             'is': [3, 8, 4, 2, 1],
             'best': [9, 5, 2, 1, 0]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extracting Dictionary values to List
# Using map()
res = list(map(list, (test_dict.values())))

# printing result
print("The list of dictionary values : " + str(res))
