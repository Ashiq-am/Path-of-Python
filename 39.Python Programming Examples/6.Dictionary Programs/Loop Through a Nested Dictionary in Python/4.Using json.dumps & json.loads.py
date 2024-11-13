import json

nested_dict = {'outer_key': {'inner_key1': 'value1', 'inner_key2': 'value2'}}
json_str = json.dumps(nested_dict)

for key, value in json.loads(json_str).items():
	print(f"Key: {key}, Value: {value}")
