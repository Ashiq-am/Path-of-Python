# initial array
arr = [[1.3, 2.5, 3.6, None],
	[2.6, 3.3, None, 5.5],
	[2.1, 3.2, 5.4, 6.5]]

# compute column means
means = []
for col in zip(*arr):
	values = [x for x in col if x is not None]
	means.append(sum(values)/len(values) if values else 0)

# replace NaN values with column means
arr = list(map(lambda row: [means[j] if x is None else x for j,x in enumerate(row)], arr))

# print final array
print(arr)
