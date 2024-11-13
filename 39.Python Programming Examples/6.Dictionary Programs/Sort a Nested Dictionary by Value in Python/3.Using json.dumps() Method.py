import json

nested_dict = {3: {'key': 3}, 1: {'key': 1}, 2: {'key': 2}}

sorted_dict = json.loads(json.dumps(nested_dict, sort_keys=True))
print(sorted_dict)
