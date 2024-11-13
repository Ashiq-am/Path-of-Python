def recursive_parser(data, keys):
	if not keys:
		return data
	return recursive_parser(data.get(keys[0], {}), keys[1:])

json_data = {"name": "John", "age": 30, "address": {"city": "New York", "zipcode": "10001"}}
keys_to_extract = ['address', 'city']

result = recursive_parser(json_data, keys_to_extract)
print('City:',result)
