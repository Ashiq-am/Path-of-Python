# Original tuple of tuples
data = (
	('dog', 30),
	('cat', 20),
	('bird', 10),
	('fish', 25)
)

# Sorting: Sorting the tuples based on the second element (quantity)
data = tuple(sorted(data, key=lambda x: x[1]))

print(data)
