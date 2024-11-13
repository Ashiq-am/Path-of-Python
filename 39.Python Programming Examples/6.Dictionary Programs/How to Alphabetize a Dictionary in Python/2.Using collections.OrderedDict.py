# import OrderedDict
from collections import OrderedDict

# ordinary dictionary
my_dict = {'banana': 3, 'apple': 4, 'cherry': 2, 'date': 5}

# sorting dictionary keys
sorted_dict = OrderedDict(sorted(my_dict.items()))
print(sorted_dict)
