# defining dictionary related to GeeksforGeeks
geeks_data = {'language': 'Python',
			'framework': 'Django', 'topic': 'Data Structures'}

keys, values = zip(*geeks_data.items())

print("Keys:")
_ = [print(key) for key in keys]

print("\nValues:")
_ = [print(value) for value in values]
