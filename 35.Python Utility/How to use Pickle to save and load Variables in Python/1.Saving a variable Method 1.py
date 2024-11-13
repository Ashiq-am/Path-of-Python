import pickle

# Create a variable
myvar = [{'This': 'is', 'Example': 1}, 'of',
		'serialisation', ['using', 'pickle']]

# Use dumps() to make it serialized
serialized = pickle.dumps(myvar)

print(serialized)
