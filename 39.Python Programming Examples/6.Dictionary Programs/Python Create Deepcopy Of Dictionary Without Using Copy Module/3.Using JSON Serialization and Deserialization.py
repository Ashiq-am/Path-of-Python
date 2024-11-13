import json

# Original dictionary
original_dict = {'title': 'GeeksforGeeks',
				'website': {'category': 'Computer Science'}}

# Using JSON serialization and deserialization
copied_dict = json.loads(json.dumps(original_dict))

# Modify the copied_dict to demonstrate deep copying
copied_dict['website']['category'] = 'Programming'

# Output
print("Original Dictionary:")
print(original_dict)
print("Copied Dictionary:")
print(copied_dict)
