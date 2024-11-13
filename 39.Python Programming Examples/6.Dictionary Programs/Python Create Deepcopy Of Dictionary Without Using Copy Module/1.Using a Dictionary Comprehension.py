# Original dictionary
original_dict = {'title': 'GeeksforGeeks',
				'website': {'category': 'Computer Science'}}

# Using dictionary comprehension for deep copy
copied_dict = {key: value if not isinstance(value, dict) else {
	k: v for k, v in value.items()} for key, value in original_dict.items()}

# Modify the copied_dict to demonstrate deep copying
copied_dict['website']['category'] = 'Programming'

# Output
print("Original Dictionary:")
print(original_dict)
print("Copied Dictionary:")
print(copied_dict)
