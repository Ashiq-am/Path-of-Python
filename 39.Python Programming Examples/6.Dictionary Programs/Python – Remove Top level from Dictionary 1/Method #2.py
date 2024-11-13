# Python3 code to demonstrate working of
# Remove Top level from Dictionary
# Using ChainMap() + dict()
from collections import ChainMap

# initializing dictionary
test_dict = {'gfg': {'data1': [4, 5, 6, 7]},
             'is': {'data2': [1, 3, 8]},
             'best': {'data3': [9, 10, 13]}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Remove Top level from Dictionary
# Using ChainMap() + dict()
res = dict(ChainMap(*test_dict.values()))

# printing result
print("The top level removed dictionary is : " + str(res))
