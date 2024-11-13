from collections import OrderedDict
from itertools import islice

# Original Dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Use OrderedDict and islice for slicing
sliced_dict = dict(islice(OrderedDict(original_dict).items(), 1, 4))

# Result
print("Original Dictionary:", original_dict)
print("Sliced Dictionary:", sliced_dict)
