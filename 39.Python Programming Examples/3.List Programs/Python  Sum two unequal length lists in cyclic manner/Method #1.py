# Python code to add two different
# length lists in cyclic manner

# Importing
from itertools import cycle

# List initialization
list1 = [150, 177, 454, 126]
list2 = [9, 44, 2, 168, 66, 80, 123, 6, 180, 184]

# Using zip
output = [x + y for x, y in zip(cycle(list1), list2)]

# Printing output
print(output)
