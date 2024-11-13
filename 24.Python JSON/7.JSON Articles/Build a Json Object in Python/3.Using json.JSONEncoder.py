import json

def encoder(obj):
	if isinstance(obj, set):
		return list(obj)
	return obj

gfg = [('name', 'Hustlers'), ('age', 19), ('is_student', True)]
json_data = dict(gfg)

json_string = json.dumps(json_data, default=encoder)
print(type(json_string))

print(json_string)
