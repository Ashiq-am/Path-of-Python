import json

json_data = '{"name": "John", "age": 30, "address": {"city": "New York", "zipcode": "10001"}}'
parsed_data = json.loads(json_data)

print('Name:',parsed_data['name'])
print('Address:',parsed_data['address']['city'])
