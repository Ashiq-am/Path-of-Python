# import OS module
import os

# This is my path
path="C://Users//Vanshi//Desktop//gfg"

# Scan the directiory and get
# an iterator of os.DirEntry objets
# corresponding to entries in it
# using os.scandir() method
obj = os.scandir()

# List all files and diretories in the specified path
print("Files and Directories in '% s':" % path)
for entry in obj:
	if entry.is_dir() or entry.is_file():
		print(entry.name)
