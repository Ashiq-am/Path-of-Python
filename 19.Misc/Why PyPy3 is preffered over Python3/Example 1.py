import os


# Race condition
File_name ="test.txt"

if os.access(File_name, os.R_ok):
	with open(File_name) as f:
		print(f.read())
else:
	print("No such file accessed")
