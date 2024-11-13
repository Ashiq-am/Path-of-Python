# Python code to convert list of tuple into list

import operator
from functools import reduce

# List of tuple initialization
tup = [(1, 2), (3, 4), (5, 6)]

# printing output
print(list(reduce(operator.concat, tup)))
