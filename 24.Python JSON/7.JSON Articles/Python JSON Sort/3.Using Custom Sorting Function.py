import json

# Sample JSON array of dictionaries
json_array = '[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 22}]'

# Parse JSON into a Python list of dictionaries
data_list = json.loads(json_array)

# Custom sorting function based on the length of 'name'
def custom_sort(item):
	return len(item['name'])

# Sort based on the custom function
sorted_data_custom = json.dumps(sorted(data_list, key=custom_sort))

print("Sorted based on custom function:", sorted_data_custom)
