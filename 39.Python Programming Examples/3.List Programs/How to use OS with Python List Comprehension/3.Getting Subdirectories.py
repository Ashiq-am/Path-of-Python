# importing os module
import os

def get_subdirectories(parent_directory):

	# list comprehension
	subdirectories = [subdir for subdir in os.listdir(
		parent_directory) if os.path.isdir(os.path.join(parent_directory, subdir))]

	# displaying the names available
	print("List of subdirectories in the parent directory:")
	for subdir in subdirectories:
		print(subdir)


# main function
if __name__ == "__main__":
	parent_directory = "gfg"
	get_subdirectories(parent_directory)
