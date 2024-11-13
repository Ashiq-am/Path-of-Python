# path of the file
file_path = "file.txt"

# Check if the file exists and is readable.
if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
	# If the file exists and is readable, print a message that the file is readable.
	print("File is readable")
else:
	# If the file does not exist or is not readable, print a message that the file is not readable.
	print("File is not readable")
