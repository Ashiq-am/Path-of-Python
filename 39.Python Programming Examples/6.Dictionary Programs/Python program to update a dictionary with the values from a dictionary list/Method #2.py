# Python3 code to demonstrate working of
# Update dictonary with dictionary list
# Using ChainMap + ** operator
from collections import ChainMap

# initializing dictionary
test_dict = {"Gfg" : 2, "is" : 1, "Best" : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing dictionary list
dict_list = [{'for' : 3, 'all' : 7}, {'geeks' : 10}, {'and' : 1, 'CS' : 9}]

# ** operator extacts keys and re initiates.
# ChainMap is used to merge dictionary list
res = {**test_dict, **dict(ChainMap(*dict_list))}

# printing result
print("The updated dictionary : " + str(res))
