import json

def is_json_empty(json_obj):
	return json_obj == {}

json_obj = {} # Empty JSON object
print(is_json_empty(json_obj))
