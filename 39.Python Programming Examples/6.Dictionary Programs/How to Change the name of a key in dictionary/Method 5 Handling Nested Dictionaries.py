def rename_key_nested(dictionary, old_key, new_key):
    for key in list(dictionary.keys()):
        if isinstance(dictionary[key], dict):
            rename_key_nested(dictionary[key], old_key, new_key)
        if key == old_key:
            dictionary[new_key] = dictionary.pop(old_key)

# Original nested dictionary
nested_dict = {
    'level1': {
        'old_key': 'value',
        'level2': {
            'old_key': 'value2'
        }
    }
}

# Rename 'old_key' to 'new_key' in nested dictionary
rename_key_nested(nested_dict, 'old_key', 'new_key')

print(nested_dict)
