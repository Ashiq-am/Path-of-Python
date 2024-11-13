# importing the module
import json
try:
	from types import SimpleNamespace as Namespace
except ImportError:
	from argparse import Namespace

# creating the data
data = '{"name" : "GeekNamespace", "id" : 3, "location" : "Bangalore"}'

# creating the object
x = json.loads(data, object_hook = lambda d : Namespace(**d))

# accessing the JSON data as an object
print(x.name, x.id, x.location)
