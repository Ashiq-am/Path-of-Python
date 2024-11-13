sorted_data_tuples = sorted([(x['age'],
							x['score'],
							x) for x in data])

# Extract the dictionaries from the sorted tuples
sorted_data = [x[2] for x in sorted_data_tuples]

# Print the sorted result
print(sorted_data)
