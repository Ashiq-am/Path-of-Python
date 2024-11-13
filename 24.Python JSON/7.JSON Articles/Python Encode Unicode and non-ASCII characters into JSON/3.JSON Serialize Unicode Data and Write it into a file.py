import json

data = {'name': 'école'}

# Open a file for writing
with open('data.json', 'w', encoding='utf-8') as f:
	# Serialize the data and write it to the file
	json.dump(data, f, ensure_ascii=False)
