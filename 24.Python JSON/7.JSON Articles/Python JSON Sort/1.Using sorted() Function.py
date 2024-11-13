import json

# Sample JSON data
json_data = '{"c": 3, "a": 1, "b": 2}'

# Parse JSON into a Python dictionary
data_dict = json.loads(json_data)

# Sort based on keys
sorted_data_keys = json.dumps({k: data_dict[k] for k in sorted(data_dict)})

# Sort based on values
sorted_data_values = json.dumps({k: v for k, v in sorted(data_dict.items(), key=lambda item: item[1])})

print("Sorted based on keys:", sorted_data_keys)
print("Sorted based on values:", sorted_data_values)
