# import shutil module
import shutil

# import os module
import os

# base path
base_path = 'C:/Users/Pulkit/GFG_Articles/root'

# list of directories we want to move.
dir_list = ['test2', 'test4', 'test5', 'does_not_exist']

# path to destination directory
dest = os.path.join(base_path, 'dest')

print("Before moving directories:")
print(os.listdir(base_path))

# traverse each directory in dir_list
for dir_ in dir_list:

	# create path to the directory in the
	# dir_list.
	source = os.path.join(base_path, dir_)

	# check if it is an existing directory
	if os.path.isdir(source):

		# move to destination path
		shutil.move(source, dest)

print("After moving directories:")
print(os.listdir(base_path))
