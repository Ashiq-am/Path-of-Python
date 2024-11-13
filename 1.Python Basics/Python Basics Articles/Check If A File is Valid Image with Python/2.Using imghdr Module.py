import os
import imghdr

# Directory path
directory_path = r"C:\Users\shrav\Desktop\GFG"

# File names
file_names = ["GFG.txt", "GFG.jpg"]

# Get full file paths
file_paths = [os.path.join(directory_path, file_name)
			for file_name in file_names]

# 2. Using imghdr


def is_valid_image_imghdr(file_name):
	with open(file_name, 'rb') as f:
		header = f.read(32) # Read the first 32 bytes
		return imghdr.what(None, header) is not None


# Example usage
for file_name in file_names:
	print(f"File: {file_name}")
	if os.path.exists(file_name): # Check if the file exists
		print("Using imghdr:", is_valid_image_imghdr(file_name))
		print()
	else:
		print(f"File '{file_name}' not found.")
		print()
