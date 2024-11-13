from operator import itemgetter

# Sort the list by 'age' and then by 'score' using itemgetter
sorted_data = sorted(data,
					key=itemgetter('age', 'score'))

# Print the sorted result
print(sorted_data)
