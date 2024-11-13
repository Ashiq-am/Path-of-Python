# List of tuples
data = [(1, 'one'), (3, 'three'), (2, 'two')]

# Sorting by the second element of each tuple
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted by second element:", sorted_data)
