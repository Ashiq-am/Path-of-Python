# defining dictionary related to GeeksforGeeks
geeks_data = {'language': 'Python', 'framework': 'Django', 'topic': 'Data Structures'}

keys = [key for key in geeks_data.keys()]
values = [value for value in geeks_data.values()]

# Print keys
print("Keys:")
for key in keys:
	print(key)

# Print values
print("\nValues:")
for value in values:
	print(value)
