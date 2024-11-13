import json

json_string = '{"name": "GFG", "age": 19, "isStudent": true}'

data = json.loads(json_string)
print(type(json_string))

print(data)
