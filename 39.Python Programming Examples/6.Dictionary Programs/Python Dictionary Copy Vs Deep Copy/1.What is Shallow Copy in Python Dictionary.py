import copy

# Original dictionary
original_dict = {'a': 1, 'b': [1, 2, 3]}
print("Original Dictionary:", original_dict)

# Shallow copy
shallow_copy = copy.copy(original_dict)
print("Shallow Copy:", shallow_copy)

# Modifying data in shallow copy
shallow_copy['b'][1] = 4

# Printing the dictionary after change
print("Original Dictionary After Change:", original_dict)

# Printing the Copy After Change
print("Shallow Copy After Change:", shallow_copy)
