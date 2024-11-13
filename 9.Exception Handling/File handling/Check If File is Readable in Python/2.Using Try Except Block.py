# file path
file_path = "file.txt"

try:
	# We try to open the file and perform operations on it.
	with open(file_path) as file:
		# print a message indicating that the file is readable.
		print("The File is readable")
# If an IOError occurs (e.g., file not found or permission denied),
except IOError:
	# Print an error message indicating that the file is not readable.
	print("Error: File is not readable")
