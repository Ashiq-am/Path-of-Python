# Specify the size of each chunk to read
chunk_size = 10

file = open("binary_file.bin", "rb")
# Using while loop to iterate the file data
while True:
	chunk = file.read(chunk_size)
	if not chunk:
		break
	# Processing the chunk of binary data
	print(f"Read {len(chunk)} bytes: {chunk}")
