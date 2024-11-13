import shutil
import os

def copy_and_replace(source_file, destination_directory):
	filename = os.path.basename(source_file)
	destination_path = os.path.join(destination_directory, filename)
	if os.path.exists(destination_path):
		os.remove(destination_path)
	shutil.move(source_file, destination_path)
	print(f"File '{filename}' copied and replaced successfully.")

# Example usage:
source_file_path = 'main.py'
destination_directory = 'dummy'

copy_and_replace(source_file_path, destination_directory)
