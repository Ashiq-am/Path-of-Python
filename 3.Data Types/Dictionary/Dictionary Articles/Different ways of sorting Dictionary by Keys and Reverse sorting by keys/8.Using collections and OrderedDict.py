# Importing OrderedDict
from collections import OrderedDict

# Initialising a dictionary
my_dict = {"b": 2, "c": 3, "a": 1,"d":4}

# Sorting dictionary
sorted_dict = OrderedDict(sorted(my_dict.items()))

# Printing sorted dictionary
print(sorted_dict)
