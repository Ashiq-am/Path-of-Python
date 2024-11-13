import json

# JSON string
json_1 = '{"Name":"GFG", "Class": "Website", "Domain":"CS/IT", "CEO":"Sandeep Jain"}'

json_2 = '{"CEO":"Sandeep Jain", "Domain":"CS/IT","Name": "GFG","Class": "Website"}'

# Converting string into Python dictionaries
json_dict1 = json.loads(json_1)
json_dict2 = json.loads(json_2)

print(sorted(json_dict1.items()) == sorted(json_dict2.items()))
