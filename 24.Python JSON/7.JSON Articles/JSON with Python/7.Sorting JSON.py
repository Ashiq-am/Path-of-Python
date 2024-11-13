# Import required libraries
import json

# Initialize JSON data
json_data = '[ {"studentid": 1, "name": "Nikhil", "subjects":\
["Python", "Data Structures"], "company":"GFG"},\
{"studentid": 2, "name": "Nisha", "subjects":\
["Java", "C++", "R Lang"], "company":"GFG"} ]'

# Create Python object from JSON string
# data
data = json.loads(json_data)

# Pretty Print JSON
json_formatted_str = json.dumps(data, indent=4, sort_keys=True)
print(json_formatted_str)
