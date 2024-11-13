def consume_memory():
	data = 'a' * (10**8)
	while True:
		data += data

consume_memory()
