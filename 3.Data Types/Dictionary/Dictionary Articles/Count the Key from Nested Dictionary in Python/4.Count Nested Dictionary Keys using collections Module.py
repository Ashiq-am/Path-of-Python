from collections import deque
# Function to count keys in a nested dictionary using the collections module

def count_keys_collections(dictionary):
	count = 0
	queue = deque([dictionary])
	while queue:
		current_dict = queue.popleft()
		count += len(current_dict)
		queue.extend(value for value in current_dict.values()
					if isinstance(value, dict))
	return count

# Example Usage:
nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}
result = count_keys_collections(nested_dict)
print("Total number of keys in the nested dictionary:", result)
