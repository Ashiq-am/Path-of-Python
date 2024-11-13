import json

data = {'name': 'école'}

# Encode the data with the ensure_ascii
# parameter set to True
json_data = json.dumps(data,
					ensure_ascii=True)

print(json_data)
