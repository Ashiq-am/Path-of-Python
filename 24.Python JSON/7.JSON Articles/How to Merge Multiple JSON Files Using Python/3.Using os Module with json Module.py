import json
import os


def merge_json_files(directory_path):
	merged_data = []
	for filename in os.listdir(directory_path):
		if filename.endswith('.json'):
			with open(os.path.join(directory_path, filename), 'r') as file:
				data = json.load(file)
				merged_data.append(data)
	return merged_data


directory_path = "./files"
output_file = "merged.json"
merged_data = merge_json_files(directory_path)
with open(output_file, 'w') as outfile:
	json.dump(merged_data, outfile)
print(merged_data)
