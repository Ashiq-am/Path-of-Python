from functools import reduce
from operator import concat

# Sample List of Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten using functools.reduce() and operator.concat
flattened_list = reduce(concat, nested_list)

# Display the result
print("Flattened List:", list(flattened_list))
