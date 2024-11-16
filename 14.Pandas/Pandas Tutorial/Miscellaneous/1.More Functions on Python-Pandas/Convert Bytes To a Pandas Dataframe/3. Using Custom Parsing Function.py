import pandas as pd

# Sample bytes data
bytes_data = b'Name:John|Age:25|Occupation:Engineer\nName:Alice|Age:30|Occupation:Doctor\nName:Bob|Age:28|Occupation:Artist'


def parse_bytes_data(data):
	# Decode bytes data and split into records
	records = data.decode('utf-8').split('\n')
	parsed_data = []
	for record in records:
		if record: # Skip empty records
			items = record.split('|') # Split record into key-value pairs
			record_dict = {}
			for item in items:
				key, value = item.split(':') # Split key-value pair
				record_dict[key] = value
			# Append record dictionary to parsed data
			parsed_data.append(record_dict)
	return pd.DataFrame(parsed_data) # Create DataFrame from parsed data


# Convert bytes to DataFrame using custom parsing function
df_method3 = parse_bytes_data(bytes_data)

# Display the DataFrame
print(df_method3)
