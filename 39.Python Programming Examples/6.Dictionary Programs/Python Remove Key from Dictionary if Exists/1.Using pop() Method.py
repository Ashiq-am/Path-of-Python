# Original dictionary
my_dict = {'gfg': 3, 'geeks': 5, 'for': 2, 'geek': 4, 'tutorial': 8}

# Key to be removed
key_to_remove = 'geek'

# Using pop() method
removed_value = my_dict.pop(key_to_remove, None)

# Output after removal
print(f"Dictionary after removing key '{key_to_remove}': {my_dict}")
print(f"Removed value: {removed_value}")
