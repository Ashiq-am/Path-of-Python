# Python code to implement iteration
# over the ordereddict

# import required modules
from collections import OrderedDict

# create dictionary
od = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

# iterating over the ordereddict
for key, value in od.items():
	print(key, value)
