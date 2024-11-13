# import required module
import os

# assign directory
directory = 'files'

# itrate over files in
# that directory
for filename in os.scandir(directory):
	if filename.is_file():
		print(filename.path)
