# import shutil module
import shutil

# import os module
import os

# base path
base_path = 'C:/Users/Pulkit/GFG_Articles/root'

# get all directories in our base path.
all_dir = os.listdir(base_path)

# path to destination directory
dest = os.path.join(base_path, 'dest')

print("Before moving directories:")
print(os.listdir(base_path))

for dir_ in all_dir:

	# check if the dir_ follows the required
	# pattern.
	if dir_.startswith('web'):

		# create path to this directory.
		source = os.path.join(base_path, dir_)

		# move to destination path
		shutil.move(source, dest)

print("After moving directories:")
print(os.listdir(base_path))
