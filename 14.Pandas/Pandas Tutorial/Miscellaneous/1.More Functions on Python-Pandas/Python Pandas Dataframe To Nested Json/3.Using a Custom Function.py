import json

# Define a custom function to create a nested structure


def custom_nested_structure(row):
	return {'Person': {'Name': row['Name'], 'Age': row['Age']}}


# Apply the custom function to each row of the DataFrame
json_data_custom = df.apply(custom_nested_structure, axis=1).tolist()

# Convert list of dictionaries to JSON
json_output = json.dumps(json_data_custom, indent=4)

print(json_output)
