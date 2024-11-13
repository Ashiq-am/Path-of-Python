# Importing SortedDict
from sortedcontainers import SortedDict

# Initialising a dictionary
my_dict = {"b": 2, "c": 3, "a": 1,"d":4}

# Sorting dictionary
sorted_dict = SortedDict(my_dict)

# Printing sorted dictionary
print(sorted_dict)
