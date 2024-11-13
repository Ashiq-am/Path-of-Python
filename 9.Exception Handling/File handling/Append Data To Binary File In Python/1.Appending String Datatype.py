# Opening the created binary file in append mode
with open('binary_file.bin', 'ab') as file:
	# Data to append
	data = b'New data to append\n'

	# Writing the data to the file
	file.write(data)

print("Data has been appended to the binary file.")
