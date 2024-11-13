def rename_key(dictionary, old_key, new_key):
    if old_key in dictionary:
        dictionary[new_key] = dictionary.pop(old_key)

# Original dictionary
my_dict = {'old_key': 'value', 'another_key': 'another_value'}

# Rename 'old_key' to 'new_key'
rename_key(my_dict, 'old_key', 'new_key')

print(my_dict)
