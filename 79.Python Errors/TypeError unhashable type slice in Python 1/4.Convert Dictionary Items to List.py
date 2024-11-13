# Original Dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Convert dictionary items to a list and then slice
dict_items_list = list(original_dict.items())
sliced_items = dict_items_list[1:3]

# Result
print("Original Dictionary:", original_dict)
print("Sliced Items:", dict(sliced_items))
