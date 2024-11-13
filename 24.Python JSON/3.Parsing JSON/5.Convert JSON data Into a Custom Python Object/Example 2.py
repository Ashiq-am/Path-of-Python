# importing the module
import json
from collections import namedtuple

# customDecoder unction
def customDecoder(geekDict):
	return namedtuple('X', geekDict.keys())(*geekDict.values())

# creating the data
geekJsonData = '{"name" : "GeekCustomDecoder", "id" : 2, "location" : "Pune"}'

# creating the object
x = json.loads(geekJsonData, object_hook = customDecoder)

# accessing the JSON data as an object
print(x.name, x.id, x.location)
