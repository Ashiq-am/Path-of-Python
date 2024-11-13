# Python code to demonstrate
# to flatten list of dictionaries
from functools import reduce

# Initialising dictionary
ini_dict = [{'a': 1}, {'b': 2}, {'c': 3}]

# printing initial dictionary
print("initial dictionary", str(ini_dict))

# code to flatten lit of dictionary
res = reduce(lambda d, src: d.update(src) or d, ini_dict, {})

# printing result
print("result", str(res))
