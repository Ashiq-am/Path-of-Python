import json

data = {'name': 'école'}

# Encode the data with the ensure_ascii parameter set to False
json_data = json.dumps(data, ensure_ascii=False)

print(json_data)
