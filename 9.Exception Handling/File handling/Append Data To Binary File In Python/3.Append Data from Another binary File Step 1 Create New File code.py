# Creating another binary file
with open('another_binary_file.bin', 'wb') as file:
	# Sample data
	data = b'\nHello, this is another binary file!\n'

	# Writing the data to the file
	file.write(data)
