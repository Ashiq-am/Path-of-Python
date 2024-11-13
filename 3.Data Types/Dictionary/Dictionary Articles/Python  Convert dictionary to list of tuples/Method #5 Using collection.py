# Python code to convert dictionary into list of tuples

# Initialization of dictionary
dict = { 'Geeks': 10, 'for': 12, 'Geek': 31 }

# Importing
import collections

# Converting
list_of_tuple = collections.namedtuple('List', 'name value')

lists = list(list_of_tuple(*item) for item in dict.items())

# Printing list
print(lists)
