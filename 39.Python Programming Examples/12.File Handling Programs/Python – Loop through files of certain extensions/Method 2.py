# importing the module
import os

# directory name
dirname = 'D:\\AllData'

# extensions
ext = ('.exe', 'jpg')

# scanning the directory to get required files
for files in os.scandir(dirname):
	if files.path.endswith(ext):
		print(files) # printing file name
