# Saving the data from one binary file
with open('another_binary_file.bin', 'rb') as source_file:
	binary_data = source_file.read()

# Writing the data of the previous file in the original file
with open('binary_file.bin', 'ab') as destination_file:
	destination_file.write(binary_data)
