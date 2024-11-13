from itertools import chain
# Examples
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using itertools.chain() and set() constructor
result_set = set(chain(set1, set2))

# Displaying the result
print(result_set) # Output: {1, 2, 3, 4, 5}
