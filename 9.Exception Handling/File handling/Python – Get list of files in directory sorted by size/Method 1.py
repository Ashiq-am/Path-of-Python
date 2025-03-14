import os

name_of_dir = 'dir_path'

# Storing list of all files
# in the given directory in list_of_files
list_of_files = filter( lambda x: os.path.isfile
					(os.path.join(name_of_dir, x)),
						os.listdir(dir_name) )

# Sort list of file names by size
list_of_files = sorted( list_of_files,
						key = lambda x: os.stat
					(os.path.join(name_of_dir, x)).st_size)

# Iterate over sorted list of file
# names and print them along with size one by one
for name_of_file in list_of_files:
	path_of_file = os.path.join(name_of_dir, name_of_file)
	size_of_file = os.stat(path_of_file).st_size
	print(size_of_file, ' -->', name_of_file)
