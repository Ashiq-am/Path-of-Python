import copy

# Original dictionary
original_dict = {"a": 1, "b": [1, 2, 3]}
print("Original Dictionary:", original_dict)

# Perform a deep copy
deep_copy = copy.deepcopy(original_dict)
print("Deep Copy:", deep_copy)

# Modify the deep copy
deep_copy["b"][1] = 4

# Print both dictionaries to see the changes
print("Original Dictionary after modifying deep copy:", original_dict)
print("Deep Copy after modification:", deep_copy)
