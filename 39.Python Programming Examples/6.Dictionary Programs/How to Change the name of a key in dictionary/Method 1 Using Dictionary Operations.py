# Original dictionary
my_dict = {'old_key': 'value'}

# Rename 'old_key' to 'new_key'
my_dict['new_key'] = my_dict.pop('old_key')

print(my_dict)  # Output: {'new_key': 'value'}
