import os


# This Function uses os.scandir method to traverse
# folders recursively and appends the name and path of
# file/folders in name_list and path_list respectively.
def find_using_scandir(path, name_list, path_list):

	# Function returns modified name_list and path_list.
	name_list, path_list = append_path_name(
		path, name_list, path_list, False)

	for curr_path_obj in os.scandir(path):

		# If the current path is a directory then the
		# function calls itself with the directory path
		# and goes on until a file is found.
		if curr_path_obj.is_dir() == True:
			file_path = curr_path_obj.path
			find_using_scandir(file_path, name_list, path_list)
		else:

			# Appends file name and file path to
			# name_list and path_list respectively.
			file_name = curr_path_obj.name
			file_path = curr_path_obj.path
			name_list.append(file_name)
			path_list.append(file_path)
	return name_list, path_list

name_list, path_list = find_using_scandir("/content/sample_data", [], [])
print(name_list)
print(path_list)
