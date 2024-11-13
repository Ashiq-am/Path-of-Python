# Filtering using a for loop
filtered_data = []
for entry in data:
	if entry['age'] > 25:
		filtered_data.append(entry)

print(filtered_data)
