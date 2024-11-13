def consume_memory():
	data = 'a' * (10**6) # Reducing the size of the string
	while True:
		data += data

consume_memory()
