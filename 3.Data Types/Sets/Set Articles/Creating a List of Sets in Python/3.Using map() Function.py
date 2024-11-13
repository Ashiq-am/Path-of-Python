# Using the map() Function
array_of_sets = list(map(lambda i: set(range(i, i + 3)),
						range(0, 10, 3)))
print(array_of_sets)
