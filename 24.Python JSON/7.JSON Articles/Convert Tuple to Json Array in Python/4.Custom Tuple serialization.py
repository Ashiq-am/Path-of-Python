import json

physics_tuple = ('Class 9', 'Physics', 'Laws of Motion', 'Introduction', 'Newton First Law')

def serialize(obj):
	if isinstance(obj, tuple):
		return {'tuple_items': list(obj)}
	return obj

json_data = json.dumps(physics_tuple, default=serialize)

print(type(json_data))
print(json_data)
