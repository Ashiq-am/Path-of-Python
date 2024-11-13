# Python code to split the list
# by some value into two lists.

# Importing
from itertools import dropwhile

# List initialisation
lst = ['Geeks', 'forgeeks', 'is a', 'portal', 'for Geeks']

# Using dropwhile to split into second list
second_list = list(dropwhile(lambda x: x != 'forgeeks', lst))[1:]

# Using set to get difference between two lists
first_list = set(lst)-set(second_list)

# removing 'split' string
first_list.remove('forgeeks')

# converting to list
first_list = list(first_list)

# Printing first list
print(first_list)

# Printing second list
print(second_list)
