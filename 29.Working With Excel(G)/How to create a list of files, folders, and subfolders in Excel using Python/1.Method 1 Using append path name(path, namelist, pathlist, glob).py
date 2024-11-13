import os


# This function splits the path by checking
# if it is a windows os or linux os path and
# appends the name and path of directory (and
# files only for glob function).
def append_path_name(path, name_list, path_list, glob):

	# Checks if it is a windows path or linux
	# path
	if path.find("\\") > 0:

		# Splits the windows path and stores the
		# list in a temp list and appends the last
		# value of temp_list in name_list as it
		# represents the name of file/ folder and
		# also appends the path to path_list.
		temp = path.split("\\")
		name_list.append(temp[-1])
		path_list.append(path)

		# If this function is called under
		# find_using_glob then we return modified
		# path so that iglob can recursively
		# traverse the folders.
		if glob == True:
			path = os.path.join(path, "**\\*")
			return path, name_list, path_list
	else:
		# Same explanation as above but the path splitting
		# is based on Linux
		temp = path.split("/")
		name_list.append(temp[-1])
		path_list.append(path)
		if glob == True:
			path = os.path.join(path, "**/*")
			return path, name_list, path_list
	return name_list, path_list

name_list, path_list = append_path_name("/content/sample_data", [], [], False)
print(name_list)
print(path_list)
