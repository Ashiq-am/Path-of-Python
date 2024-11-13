# Function to count keys in a nested dictionary using loop
def count(dictionary):
	return (len(dictionary)+sum(count(value)
								for value in dictionary.values() if isinstance(value, dict)))


# Example Usage:
nested_dict = {'Dict1': {'name': 'Alice', 'age': '22', 'address': {'city': 'Wonderland'}},
			'Dict2': {'name': 'Bob', 'age': '28', 'contacts': {'email': 'bob@example.com'}}}

result = count(nested_dict)
print("Total number of keys in the nested dictionary:", result)
