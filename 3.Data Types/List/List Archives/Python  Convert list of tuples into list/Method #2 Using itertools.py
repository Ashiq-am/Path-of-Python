# Python code to convert list of tuple into list

# Importing
import itertools

# List of tuple initialization
tuple = [(1, 2), (3, 4), (5, 6)]

# Using itertools
out = list(itertools.chain(*tuple))

# printing output
print(out)
