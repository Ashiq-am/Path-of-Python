import os

file_path = "file.txt"

if os.access(file_path, os.R_OK):
	print("File is readable")
else:
	print("File is not readable")
