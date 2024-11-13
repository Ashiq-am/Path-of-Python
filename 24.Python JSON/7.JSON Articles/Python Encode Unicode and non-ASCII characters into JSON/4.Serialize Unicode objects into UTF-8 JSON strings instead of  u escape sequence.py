import json

data = {'name': 'école'}

# Encode the data with the encoding parameter set to 'utf-8'
json_data = json.dumps(data, encoding='utf-8', ensure_ascii=False)

print(json_data)
