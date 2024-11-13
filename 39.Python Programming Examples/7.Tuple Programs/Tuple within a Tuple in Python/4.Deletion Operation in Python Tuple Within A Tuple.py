# Original tuple of tuples
data = (
	('dog', 30),
	('cat', 20),
	('bird', 10),
	('fish', 25)
)

# Deletion: Removing the tuple containing 'bird'
data = tuple(item for item in data if item[0] != 'bird')
print(data)
