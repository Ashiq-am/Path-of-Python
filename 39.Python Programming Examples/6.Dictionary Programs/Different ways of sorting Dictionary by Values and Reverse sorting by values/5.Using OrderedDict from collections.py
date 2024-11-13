# Python program to sort dictionary
# by value using OrderedDict

# Import OrderedDict
from collections import OrderedDict

# Initialize a dictionary
my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Sort dictionary
sorted_dict = OrderedDict(sorted(my_dict.items(), key = lambda x: x[1]))

# Print the sorted dictionary
print("Sorted dcitonary is :")
print(sorted_dict)
