# Original dictionary
my_dict = {'old_key': 'value', 'another_key': 'another_value'}

# Rename 'old_key' to 'new_key'
new_dict = {'new_key' if k == 'old_key' else k: v for k, v in my_dict.items()}

print(new_dict)  # Output: {'new_key': 'value', 'another_key': 'another_value'}
