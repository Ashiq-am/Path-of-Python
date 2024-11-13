# Original dictionary
my_dict = {'old_key': 'value', 'another_key': 'another_value'}

# Create a new key-value pair and remove the old key
my_dict.update({'new_key': my_dict.pop('old_key')})

print(my_dict)  # Output: {'another_key': 'another_value', 'new_key': 'value'}
