# Original dictionary
my_dict = {'gfg': 3, 'geeks': 5, 'for': 2, 'geek': 4, 'tutorial': 8}

# Key to be removed
key_to_remove = 'geek'

# Using dictionary comprehension
my_dict = {k: v for k, v in my_dict.items() if k != key_to_remove}

# Output after removal
print(f"Dictionary after removing key '{key_to_remove}': {my_dict}")
