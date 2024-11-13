from collections import OrderedDict

# Sort the list by 'age' and then by 'score' using OrderedDict
sorted_data = sorted(data,key=lambda x: OrderedDict(sorted(x.items())))

# Print the sorted result
print(sorted_data)
