import shutil
import os

def copy_and_replace(source_path, destination_path):
	if os.path.exists(destination_path):
		os.remove(destination_path)
	shutil.copy2(source_path, destination_path)

# Source and destination file paths
source_file = 'path/to/source_file.txt'
destination_file = 'path/to/destination_file.txt'

# Copy and replace
copy_and_replace(source_file, destination_file)
