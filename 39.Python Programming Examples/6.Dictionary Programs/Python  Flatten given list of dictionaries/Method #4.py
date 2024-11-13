# Python code to demonstrate
# to flatten list of
# dictionaries

from collections import ChainMap

# Initialising dictionary
ini_dict = [{'a': 1}, {'b': 2}, {'c': 3}]

# printing initial dictionary
print("initial dictionary", str(ini_dict))

# code to flatten lit of dictionary
res = ChainMap(*ini_dict)

# printing result
print("result", str(res))
