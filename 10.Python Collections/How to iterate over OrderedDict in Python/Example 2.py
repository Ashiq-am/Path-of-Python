# Python code to implement iteration
# over the ordereddict

# import required modules
from collections import OrderedDict

# create dictionary
od = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

# iterating through the enumerate objects
for i, (key, value) in enumerate(od.items()):
	print(key, value)
