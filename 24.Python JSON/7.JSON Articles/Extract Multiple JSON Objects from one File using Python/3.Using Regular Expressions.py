# import required modules
import re
import json

# define re pattern to match Json Object
pattern = r'{.*?}'

# open a file
with open('data.json', 'r') as file:
	file_cont = file.read()

# find all JSON Objectss from a file by passing re pattern
json_objs = re.findall(pattern, file_cont)

# parse each JSON object
for obj_string in json_objs:
	obj = json.loads(obj_string)
	print(obj)
