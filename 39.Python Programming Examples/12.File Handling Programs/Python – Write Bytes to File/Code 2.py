some_bytes = b'\x21'

# Open file in binary write mode
binary_file = open("my_file.txt", "wb")

# Write bytes to file
binary_file.write(some_bytes)

# Close file
binary_file.close()
