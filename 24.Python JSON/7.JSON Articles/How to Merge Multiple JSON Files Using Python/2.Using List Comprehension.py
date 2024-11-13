import json
def merge_json_files(file_paths):
	merged_data = [json.load(open(path, 'r')) for path in file_paths]
	return merged_data


file_paths = ["f.json", "s.json","e.json","t.json"]
output_file = "merged.json"
merged_data = merge_json_files(file_paths)
with open(output_file, 'w') as outfile:
	json.dump(merged_data, outfile)
print(merged_data)
