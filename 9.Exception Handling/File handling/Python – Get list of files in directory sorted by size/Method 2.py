import glob
import os

name_of_dir = 'dir_path/'

# Storing list of all files (file paths)
# in the given directory in list_of_files
list_of_files = filter( os.path.isfile,
						glob.glob(name_of_dir + '*') )

# Sort list of files in directory by size
list_of_files = sorted( list_of_files,
						key = lambda x: os.stat(x).st_size)

# Iterate over sorted list of file names
# and print them along with size one by one
for path_of_file in list_of_files:
	size_of_file = os.stat(path_of_file).st_size
	print(size_of_file, ' -->', path_of_file)
