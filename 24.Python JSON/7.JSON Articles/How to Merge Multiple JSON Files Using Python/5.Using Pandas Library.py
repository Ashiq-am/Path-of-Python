import pandas as pd
import json


def merge_json_files(file_paths):
	merged_data = pd.DataFrame()
	for path in file_paths:
		with open(path, 'r') as file:
			data = json.load(file)
			row = pd.DataFrame([data])
			merged_data = pd.concat([merged_data, row], ignore_index=True)
	return merged_data


file_paths = ["f.json", "s.json", "e.json", "t.json"]
output_file = "merged.json"

merged_data = merge_json_files(file_paths)

merged_data.to_json(output_file, orient='records')

print(merged_data)
