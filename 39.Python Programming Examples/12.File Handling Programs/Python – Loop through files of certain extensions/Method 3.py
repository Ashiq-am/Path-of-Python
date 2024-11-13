# importing the module
import os

# giving directory name
folderdir = 'D:\\AllData'

# giving file extensions
ext = ('.pdf', '.mkv')

# iterating over directory and subdirectory to get desired result
for path, dirc, files in os.walk(folderdir):
	for name in files:
		if name.endswith(ext):
			print(name) # printing file name
