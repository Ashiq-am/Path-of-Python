data = [1, 2, 3, 4, 5]

# Opening the same binary file in append mode
with open('binary_file.bin', 'ab') as file:
	# Converting integers to bytes and append to the file
	for num in data:
		file.write(num.to_bytes(4, byteorder='big'))
