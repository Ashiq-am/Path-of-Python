# Sort the list by 'age' and then by 'score'
sorted_data = sorted(data, key=lambda x: (x['age'],
										x['score']))

# Print the sorted result
print(sorted_data)
