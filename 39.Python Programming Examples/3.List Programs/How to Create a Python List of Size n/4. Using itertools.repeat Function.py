import itertools

# Define the size of the list
size = 5
default_value = 'None'

# Create a list with the specified size filled with a default value using itertools
my_list = list(itertools.islice(itertools.repeat(default_value), size))

print(my_list)
