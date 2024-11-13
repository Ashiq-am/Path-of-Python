# Python program to sort dictionary
# by value using OrderedDict

# Import Counter
from collections import Counter

# Initialize a dictionary
my_dict = {'hello': 1, 'python': 5, 'world': 3}

# Sort and print the dictionary
sorted_dict = Counter(my_dict)
print("Sorted dictionary is :")
print(sorted_dict.most_common()[::-1])
