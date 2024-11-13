from itertools import chain

# Sample List of Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten using itertools.chain()
flattened_list = list(chain(*nested_list))

# Display the result
print("Flattened List:", flattened_list)
