# Filtering function
def filter_by_age(entry):
	return entry['age'] > 25

# Using filter function
filtered_data = list(filter(filter_by_age, data))

print(filtered_data)
